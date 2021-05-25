for (const links of document.getElementsByClassName('referral-links')) {
  const index = Math.floor(Math.random() * links.children.length);
  links.children[index].style.display = 'inherit';
}
