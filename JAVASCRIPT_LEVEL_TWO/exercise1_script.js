function sleepIn(weekday, vacation){
  if(weekday == true && vacation == false){
    return false;
  }else if (weekday == false && vacation ==false) {
    return true;
  }else if (weekday == false && vacation == true) {
    return true;
  }
}
