var default_bgdropdown_color = 0;
function mouseOver(index){
  default_bgdropdown_color = document.getElementsByClassName("dropdown-item")[index].style.backgroundColor;
  document.getElementsByClassName("dropdown-item")[index].style.backgroundColor = "#0BB48B";
}
function mouseOut(index) {
  document.getElementsByClassName("dropdown-item")[index].style.backgroundColor = default_bgdropdown_color;
}
