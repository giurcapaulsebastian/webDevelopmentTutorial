var firstname = prompt("Please enter your firstname");
var lastname = prompt("Please enter your lastname");
var age = prompt("Please enter your age");
var height = prompt("Please enter your height(in cm)");
var petName = prompt("Please enter your pet's name");

if(firstname[0] === lastname[0] && age >20 && age < 30 && height>=170 && petName[petName.length-1] == "y"){
  console.log("This is your secret message!");
}
