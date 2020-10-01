var employee={
  name:"John Smith",
  job: "Programmer",
  age: 31,
  // nameLength: function(){
  //   console.log(this.name.length);
  // }
  lastName:function(){
    var res = this.name.split(" ");
    console.log(res[1]);
  }
}

// employee.nameLength();
employee.lastName();
// for (var k in employee) {
//   alert(k + " is " + employee[k]);
// }
