(() => {
  document.querySelectorAll('[data-cte-explorer]').forEach((explorer) => {
    const detail = explorer.querySelector('.cte-explorer__detail');
    const buttons = Array.from(explorer.querySelectorAll('[data-cte-target]'));
    const blocks = Array.from(explorer.querySelectorAll('[data-cte-block]'));
    const templates = new Map(
      Array.from(explorer.querySelectorAll('template[data-cte-detail]')).map((template) => [
        template.dataset.cteDetail,
        template,
      ]),
    );

    if (!detail || !buttons.length) return;

    const select = (key, updateHash = true) => {
      const template = templates.get(key);
      if (!template) return;

      detail.innerHTML = template.innerHTML;
      buttons.forEach((button) => {
        const active = button.dataset.cteTarget === key;
        button.setAttribute('aria-pressed', String(active));
      });
      blocks.forEach((block) => {
        block.classList.toggle('is-active', block.dataset.cteBlock === key);
      });

      if (updateHash) {
        history.replaceState(null, '', `${window.location.pathname}${window.location.search}#${key}`);
      }
    };

    buttons.forEach((button) => {
      button.addEventListener('click', () => select(button.dataset.cteTarget));
    });

    const requested = window.location.hash.slice(1);
    const initial = templates.has(requested) ? requested : buttons[0].dataset.cteTarget;
    select(initial, false);
  });
})();
