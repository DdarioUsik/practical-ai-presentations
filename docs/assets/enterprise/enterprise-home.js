(() => {
  const form = document.querySelector("#enterprise-assessment-form");
  const inputs = [...document.querySelectorAll("[data-calc]")];
  const capacityOut = document.querySelector("#ea-capacity");
  const valueOut = document.querySelector("#ea-value");
  const locale = document.documentElement.lang === "ru" ? "ru-RU" : "en-IE";

  const emit = (name) => {
    const detail = { event: name };
    document.dispatchEvent(new CustomEvent("practical_ai_event", { detail }));
    if (Array.isArray(window.dataLayer)) window.dataLayer.push(detail);
  };

  const valueOf = (key, fallback = 0) => {
    const field = inputs.find((input) => input.dataset.calc === key);
    const value = field ? Number(field.value) : fallback;
    return Number.isFinite(value) ? Math.max(0, value) : fallback;
  };

  const updateEstimate = () => {
    if (!capacityOut || !valueOut) return;
    const capacity = valueOf("users") * (valueOf("adoption") / 100) * valueOf("hours") * valueOf("weeks");
    const monetaryEquivalent = capacity * valueOf("hourly");
    const numberFormat = new Intl.NumberFormat(locale, { maximumFractionDigits: 0 });
    const currencyFormat = new Intl.NumberFormat(locale, {
      style: "currency", currency: "EUR", maximumFractionDigits: 0,
    });
    capacityOut.textContent = `${numberFormat.format(capacity)} ${locale.startsWith("ru") ? "ч" : "h"}`;
    valueOut.textContent = currencyFormat.format(monetaryEquivalent);
  };

  inputs.forEach((input) => input.addEventListener("input", updateEstimate));
  updateEstimate();

  document.querySelectorAll(".enterprise-mobile-menu a[href^='#']").forEach((link) => {
    link.addEventListener("click", () => {
      const menu = link.closest("details");
      if (menu) menu.open = false;
    });
  });

  document.querySelectorAll("[data-event]").forEach((element) => {
    element.addEventListener("click", () => emit(element.dataset.event));
  });

  document.querySelectorAll(".enterprise-header .button, .ea-actions a, .ea-case-card a, .ea-final .button").forEach((element) => {
    element.addEventListener("click", () => {
      const href = element.getAttribute("href") || "";
      emit(href.includes("/cases/") ? "case_details_click" : href.includes("#assessment") ? "assessment_cta" : "homepage_navigation");
    });
  });

  if (form) {
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const data = new FormData(form);
      const lang = form.dataset.lang;
      const message = lang === "ru"
        ? [
            "Здравствуйте, Данил. Хочу обсудить AI Opportunity & Readiness Assessment для нашей компании.",
            `Компания: ${data.get("company")}`,
            `Рабочая почта: ${data.get("email")}`,
            data.get("role") ? `Роль: ${data.get("role")}` : "",
            data.get("process") ? `Процесс для улучшения: ${data.get("process")}` : "",
          ].filter(Boolean).join("\n")
        : [
            "Hello Danil. I’d like to discuss the AI Opportunity & Readiness Assessment for our company.",
            `Company: ${data.get("company")}`,
            `Work email: ${data.get("email")}`,
            data.get("role") ? `Role: ${data.get("role")}` : "",
            data.get("process") ? `Process to improve: ${data.get("process")}` : "",
          ].filter(Boolean).join("\n");
      const status = document.querySelector("#ea-form-status");
      if (status) status.textContent = lang === "ru"
        ? "Откроется WhatsApp с вашим черновиком. Проверьте данные и отправьте сообщение там."
        : "WhatsApp will open with your draft. Review the details and send it there.";
      emit("assessment_whatsapp_draft");
      window.location.assign(`https://wa.me/34627184000?text=${encodeURIComponent(message)}`);
    });
  }
})();
