var table = document.getElementById('center')

console.log("CONNECTED");

if(table!=null){
  for (var i = 0; i < table.rows.length; i++) {
    for (var j = 0; j < table.rows[i].cells.length; j++) {
      table.rows[i].cells[j].onclick = function(){
        tableText(this);
      };
    }
  }
}

function tableText(tableCell) {
  if(tableCell.innerHTML==" "){
    tableCell.innerHTML = "X"
  }
  else if(tableCell.innerHTML == "X"){
    tableCell.innerHTML = "O"
  }else if (tableCell.innerHTML == "O") {
    tableCell.innerHTML = " "
  }
}
