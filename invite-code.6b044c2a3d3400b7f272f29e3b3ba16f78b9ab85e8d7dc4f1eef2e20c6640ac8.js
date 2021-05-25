for (const codes of document.getElementsByClassName('invite-code')) {
  const index = Math.floor(Math.random() * codes.children.length);
  codes.children[index].style.display = 'inherit';
}
