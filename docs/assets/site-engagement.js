(() => {
  const lang = document.documentElement.lang === "ru" ? "ru" : "en";
  const messages = {
    en: ["Hello Danil. I’d like to discuss AI training for our school.", "School", "Participants", "Staff roles", "Training language", "Preferred start"],
    ru: ["Здравствуйте, Данил. Хочу обсудить обучение команды школы работе с ИИ.", "Школа", "Участники", "Роли", "Язык обучения", "Желаемый старт"],
  };
  function track(name) {
    document.dispatchEvent(new CustomEvent("practical_ai_event", { detail: { event: name } }));
  }

  document.addEventListener("click", event => {
    const link = event.target.closest("a[href]");
    if (!link) return;
    const url = new URL(link.href);
    if (url.protocol === "mailto:") track("contact_email_click");
    else if (["wa.me", "t.me", "www.linkedin.com"].includes(url.hostname)) track("contact_message_click");
    else if (link.dataset.contact === "form" || url.hash === "#assessment-form" ||
      (document.body.classList.contains("school-page") && url.hash === "#contact")) track("contact_form_open");
  });

  const schoolForm = document.querySelector("#school-intake-form[data-school-language]");
  schoolForm?.addEventListener("submit", event => {
    event.preventDefault();
    const values = new FormData(schoolForm);
    const [greeting, ...labels] = messages[lang];
    const fields = ["school", "participants", "roles", "language", "start"];
    const lines = fields.flatMap((key, i) => values.get(key) ? [labels[i] + ": " + values.get(key)] : []);
    const url = "https://wa.me/34627184000?text=" + encodeURIComponent([greeting, ...lines].join("\n"));
    window.open(url, "_blank", "noopener,noreferrer");
  });
  document.querySelector("#school-intake-form")?.addEventListener("submit", () => track("school_whatsapp_draft"));

  // Only load GA4 once the owner has configured a property and the visitor opts in.
  const id = document.querySelector('meta[name="pa-ga4-id"]')?.content;
  if (!/^G-[A-Z0-9]+$/.test(id || "")) return;
  const key = "practical-ai-analytics-consent";
  const host = document.querySelector("#pa-contact-links");
  if (!host) return;
  const options = document.createElement("div");
  options.className = "pa-analytics-settings";
  const label = document.createElement("span");
  label.textContent = lang === "ru" ? "Аналитика посещений" : "Visit analytics";
  const allow = document.createElement("button");
  allow.type = "button";
  allow.textContent = lang === "ru" ? "Разрешить" : "Allow";
  const deny = document.createElement("button");
  deny.type = "button";
  deny.textContent = lang === "ru" ? "Отключить" : "Disable";
  options.append(label, allow, deny);
  host.after(options);

  let loaded = false;
  function update(choice) {
    window["ga-disable-" + id] = choice !== "yes";
    allow.setAttribute("aria-pressed", String(choice === "yes"));
    deny.setAttribute("aria-pressed", String(choice === "no"));
    if (choice !== "yes" || loaded) return;

    loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", id, {
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
      page_location: location.origin + location.pathname,
      page_referrer: "",
    });
    const script = document.createElement("script");
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(id);
    document.head.append(script);
  }
  function save(choice) {
    try { localStorage.setItem(key, choice); } catch {}
    update(choice);
  }
  allow.addEventListener("click", () => save("yes"));
  deny.addEventListener("click", () => save("no"));
  let choice;
  try { choice = localStorage.getItem(key); } catch {}
  update(choice);
  const events = new Set(["contact_email_click", "contact_message_click", "contact_form_open",
    "school_whatsapp_draft", "assessment_whatsapp_draft"]);
  document.addEventListener("practical_ai_event", event => {
    const name = event.detail?.event;
    if (loaded && !window["ga-disable-" + id] && events.has(name)) window.gtag("event", name);
  });
})();
