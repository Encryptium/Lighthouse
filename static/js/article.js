var progress = document.createElement('progress');

progress.id = 'article-progress';
progress.max = 100;
progress.value = 0;

document.body.appendChild(progress);

window.onscroll = function() {scrollUpdate()};

function scrollUpdate() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  progress.value = scrolled;
}