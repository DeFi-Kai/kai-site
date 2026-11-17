(() => {
  const viewer = document.querySelector('.image-viewer');
  if (!viewer || typeof viewer.showModal !== 'function') return;

  const expandedImage = viewer.querySelector('.image-viewer-image');
  const closeButton = viewer.querySelector('.image-viewer-close');
  let activeImage;

  const openImage = (image) => {
    activeImage = image;
    expandedImage.src = image.currentSrc || image.src;
    expandedImage.alt = image.alt;
    viewer.showModal();
    document.documentElement.classList.add('image-viewer-open');
  };

  document.querySelectorAll('.post-single .post-content img').forEach((image) => {
    if (image.closest('a, button')) return;

    image.classList.add('image-expandable');
    image.tabIndex = 0;
    image.setAttribute('role', 'button');
    image.setAttribute('aria-haspopup', 'dialog');
    image.setAttribute('aria-label', image.alt ? `Enlarge image: ${image.alt}` : 'Enlarge image');
    image.addEventListener('click', () => openImage(image));
    image.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        openImage(image);
      }
    });
  });

  closeButton.addEventListener('click', () => viewer.close());
  viewer.addEventListener('click', (event) => {
    if (event.target === viewer) viewer.close();
  });
  viewer.addEventListener('close', () => {
    document.documentElement.classList.remove('image-viewer-open');
    expandedImage.removeAttribute('src');
    activeImage?.focus({ preventScroll: true });
  });
})();
