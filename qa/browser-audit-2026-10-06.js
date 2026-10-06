async (page) => {
  const base = 'http://127.0.0.1:8791';
  const core = ['/', '/ru/', '/about/', '/ru/about/', '/programs/', '/ru/programs/', '/for-hr/', '/ru/for-hr/', '/blog/', '/ru/blog/', '/blog/corporate-ai-training/', '/ru/blog/corporate-ai-training/', '/blog/ai-for-project-managers/', '/ru/blog/ai-for-project-managers/', '/blog/ai-for-finance-teams/', '/ru/blog/ai-for-finance-teams/', '/blog/ai-my-voice/'];
  const cases = ['01-kpi-partners', '01-voice-ai-assistant-n8n', '02-pdf-linguist', '03-multitenant-textanalytics', '04-telegram-monitoring', '05-360-johari', '06-kyb', '07-robotmonitoring', '08-resumescreening'];
  const legacy = ['/cases/', ...cases.map(x => '/cases/' + x + '/'), '/aihub/', '/vedenina/', '/welcs/', '/drhead/', '/crm/', '/offers/', '/community-sprint/', '/vibe-salon/', '/capital_group_2026-03-06_cases.html'];
  const problems = [], results = [];
  let pageErrors = [];
  page.on('pageerror', error => pageErrors.push(error.message));
  for (const width of [320, 375, 768, 1440]) {
    await page.setViewportSize({width, height: 900});
    for (const route of (width === 1440 ? [...core, ...legacy] : core)) {
      pageErrors = [];
      try {
      const response = await page.goto(base + route, {waitUntil: 'load', timeout: 20000});
      if (route === '/offers/') await page.waitForURL(base + '/cases/', {waitUntil: 'load'});
      if (route === '/community-sprint/') await page.waitForURL(base + '/', {waitUntil: 'load'});
      await page.evaluate(() => { for (const img of document.images) img.loading = 'eager'; });
      await page.waitForFunction(() => [...document.images].every(img => img.complete), null, {timeout: 4000}).catch(() => {});
      const state = await page.evaluate(() => {
        const contact = document.querySelector('.nav-end a[href^="https://wa.me/"]');
        const box = contact?.getBoundingClientRect();
        return {
          overflow: document.documentElement.scrollWidth > innerWidth + 1,
          brokenImages: [...document.images].filter(img => img.complete && !img.naturalWidth).map(img => img.getAttribute('src')),
          visibleHeaderContact: box ? box.width > 0 && box.height >= 44 && box.right <= innerWidth + 1 : null,
          headerHeight: document.querySelector('.site-header')?.getBoundingClientRect().height,
          teamPortraits: [...document.querySelectorAll('.team-portrait img')].filter(img => img.naturalWidth === 400).length,
        };
      });
      results.push({route, width, status: response?.status(), ...state});
      if (response?.status() >= 400 || state.overflow || state.brokenImages.length || pageErrors.length || (core.includes(route) && state.visibleHeaderContact !== true)) {
        problems.push({route, width, status: response?.status(), ...state, pageErrors});
      }
      } catch (error) {
        problems.push({route, width, error: error.message, finalUrl: page.url()});
      }
    }
  }
  await page.goto(base + '/');
  await page.keyboard.press('Tab');
  const skipFocused = await page.evaluate(() => document.activeElement.classList.contains('skip-link'));
  await page.keyboard.press('Enter');
  const skipWorks = await page.evaluate(() => document.activeElement.id === 'main-content');
  if (!skipFocused || !skipWorks) problems.push({keyboardSkip: {skipFocused, skipWorks}});
  return {checks: results.length, problems, keyboardSkip: {skipFocused, skipWorks}, headerHeights: results.filter(x => x.route === '/').map(x => ({width:x.width, height:x.headerHeight})), allTeamPortraitsLoaded: results.filter(x => ['/', '/ru/', '/about/', '/ru/about/'].includes(x.route)).every(x => x.teamPortraits === 3)};
}
