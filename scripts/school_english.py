"""English copy for the private schools programme."""


def school_page_en() -> str:
    return '''
<section class="hero school-hero"><div class="wrap school-hero-grid">
  <div class="school-hero-copy">
    <span class="eyebrow">Professional development for private schools</span>
    <h1>Give your school team four weeks to put AI into practice.</h1>
    <p class="hero-lede">Teachers, academic leads and administrators each build and test an AI assistant for a task they already do.</p>
    <div class="hero-actions"><a class="button button--dark" href="#contact">Discuss the programme</a><a class="button button--light" href="#program">See how it works ↓</a></div>
    <p class="hero-note">Sessions run online. On-site training can be arranged separately.</p>
  </div>
  <aside class="school-offer-card school-result-card">
    <img class="school-brand-art" src="/assets/brand/glass/school.webp" alt="" width="418" height="418">
    <span class="school-offer-label">What your team takes away</span>
    <strong class="school-offer-price">AI assistants built for school work</strong>
    <p>Each participant leaves with a tested workflow and a way to check its output.</p>
  </aside>
</div></section>
<section class="section school-role-section" id="program"><div class="wrap">
  <div class="section-head"><h2>Start with the work each team already does</h2></div>
  <div class="school-role-grid">
    <article class="school-role-card"><h3>Teachers</h3><p>Draft differentiated assignments, assessment criteria and feedback. Teachers check each draft against the curriculum before using it.</p></article>
    <article class="school-role-card"><h3>Academic leads</h3><p>Organise teaching materials, prepare reports and review anonymised information about learning. Academic leads check the conclusions against school records.</p></article>
    <article class="school-role-card"><h3>Leadership and administration</h3><p>Summarise approved documents, prepare questions for meetings and draft internal guidance. School leaders review the evidence and make the decisions.</p></article>
  </div>
</div></section>
<section class="section school-demos" id="examples"><div class="wrap">
  <div class="section-head"><h2>Two examples from a school workday</h2><p>Both examples use fictional data.</p></div>
  <div class="school-demo-grid">
    <details class="school-demo-card">
      <summary class="school-demo-head"><span>For a teacher</span></summary>
      <div class="school-demo-content">
        <h3>Water cycle activities for Year 5</h3>
        <div class="school-demo-flow">
          <div><b>The task</b><p>Design three activities for the same learning objective, at different levels of difficulty.</p></div>
          <div class="school-artifact"><b>AI draft</b><ol>
            <li>Foundation: put the stages of the water cycle in order.</li>
            <li>Core: explain how water from a puddle evaporates and becomes part of a cloud.</li>
            <li>Extension: design an experiment that demonstrates evaporation and condensation.</li>
          </ol></div>
          <div><b>Teacher review</b><p>Check each activity against the lesson objective, pupils’ age and the curriculum. Adjust the wording where needed.</p></div>
        </div>
      </div>
    </details>
    <details class="school-demo-card">
      <summary class="school-demo-head"><span>For a school director</span></summary>
      <div class="school-demo-content">
        <h3>Prepare questions for a school budget review</h3>
        <div class="school-demo-flow">
          <div><b>The task</b><p>Use an approved spreadsheet with planned and actual spending to prepare a short note for the budget meeting.</p></div>
          <div class="school-artifact"><b>Excerpt from the AI draft</b><p>“Spending on teaching materials was 6 units over budget. Ask the person responsible when the purchases were made and what drove the difference.”</p></div>
          <div><b>Director review</b><p>Check the figure against the spreadsheet, confirm the context and decide which questions to raise.</p></div>
        </div>
      </div>
    </details>
  </div>
</div></section>
<section class="section school-month" id="month"><div class="wrap">
  <div class="section-head"><h2>Four weeks from task to tested assistant</h2><p>Before training, we interview school leaders and staff, identify priorities and agree the tools and data participants can use.</p></div>
  <div class="school-week-grid">
    <article><span>Week 1</span><h3>Choose the task</h3><p>Agree what a good result looks like.</p></article>
    <article><span>Week 2</span><h3>Build the assistant</h3><p>Prepare instructions and approved examples.</p></article>
    <article><span>Week 3</span><h3>Try it in practice</h3><p>Check outputs against the original materials and refine the workflow.</p></article>
    <article><span>Week 4</span><h3>Show how it works</h3><p>Demonstrate the assistant and explain how colleagues can review its output.</p></article>
  </div>
</div></section>
<section class="section school-pricing-section" id="pricing"><div class="wrap">
  <div class="section-head"><h2>Programme fees</h2></div>
  <div class="school-pricing-grid">
    <article class="school-price-card"><span>School assessment</span><strong>€2,000</strong><p>We map the school’s workflows, recommend priorities and propose training groups. If you sign a training agreement, we credit the assessment fee towards the programme.</p></article>
    <article class="school-price-card"><span>Training per participant</span><strong>$700</strong><p>Eight hours of live online sessions and about ten hours of practice. We confirm the total after assessment, based on group size and the number of cohorts.</p></article>
  </div>
  <a class="school-download-link school-download-link--dark" href="/assets/downloads/practical-ai-school-program.pdf" download>Download the programme PDF (in Russian) ↓</a>
</div></section>
<section class="closing school-closing" id="contact"><div class="wrap closing-inner">
  <div class="closing-copy"><h2>Discuss the programme for your school</h2><p>Tell us which staff would take part, your preferred training language and when you would like to start.</p></div>
  <form class="school-intake-form" id="school-intake-form" data-school-language="en">
    <label>School name<input name="school" autocomplete="organization" required></label>
    <label>Expected number of participants<input name="participants" type="number" min="1" inputmode="numeric"></label>
    <label>Which staff will take part?<input name="roles" placeholder="Teachers, leaders, administrators"></label>
    <label>Preferred training language<input name="language"></label>
    <label>Preferred start date<input name="start"></label>
    <div class="school-form-actions"><button class="button button--dark" type="submit">Prepare WhatsApp message</button></div>
    <p class="school-cta-status">You can review the draft in WhatsApp before sending.</p>
  </form>
</div></section>'''
