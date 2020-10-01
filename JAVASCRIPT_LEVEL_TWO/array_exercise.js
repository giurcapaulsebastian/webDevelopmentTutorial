var roster=[];

function addNew(name){
  roster.push(name);
}

function remove(name){
  for (var i = 0; i < roster.length; i++) {
    if(roster[i]==name){
      roster.splice(i,1);
    }
  }
}

function display(){
  for (var name of roster) {
    console.log(name);
  }
}

while(true){
  var option = prompt("Give me an option(add,remove,display,quit)");
  if(option == "add"){
    var name = prompt("Give a name:");
    addNew(name);
  }else if (option == "remove") {
    var name = prompt("Who should be deleted ?");
    remove(name);
  }else if (option == "display") {
    display();
  }else if(option=="quit"){
    break;
  }
}
