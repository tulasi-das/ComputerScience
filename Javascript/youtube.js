
// var tulasi = prompt("enter your name")
// console.log(tulasi)
// var username = "tulasi"
// var age = 4
// console.log(username+" "+age)

// function
// function blah{
//     var x = 5;
//     console.log(x);
// }
// console.log(x);

// declaring a variable in javascript

// var a;
// x = 10
// let a = 10

// primitives and objects
// {
//     let a =5;
//     let b = "dazz";
//     let c =a+" "+b;
//     console.log(c);
// }
// primitive datatypes are string, number, boolean, symbol
// in java script we can use both single and double quotes for string
// primitives are immutable in js

// object in js
//  An object is a collection of key value pairs in javascript
// ex
// let person = {
//     name: "tulasidas",
//     age:30,
//     fun: function(){               // here we declared the function fun inside the object
//         console.log("yay!");
//     }
    
// }
// person.fun();           // for accesing the function defined inside the objct we use object.function name
// console.log(person.name);   //for accesing the individual elements defined inside the obejct

// objects: everything that we creat if its not a primitive then its a object

// let now = new Date(); // now is a date type object

// let grades = [1,2,3,4,5]; // grades is an object of array type

// {
//     let myName = "tulasidas";
//     myName = myName.toUpperCase();
//     console.log(myName);
// }

// // primitives dont have any methods, it is boxed into another object and returns the primitive after performing the operations

// let age =new Number();   //here age is object type

// console.log(typeof(age));
// // console.log(age);
// let b = age.valueOf();     // here is b is of primitive type
// // console.log(b);
// console.log(typeof(b));


// in javascript we have NaN(Not a number), Infinity we dont get any runtime exception

// {
//     console.log(1/0);    //here we get the value infinity we dont get any run time exception like in java
// }

// {
//     console.log(console.log()+console.log()); //it gives not a number
// }

// parse int and parse float for converting the string into Number

// {
//     let x = 14;
//     let y = "20";
//     let z = x + Number.parseInt(y);
//     console.log(z);  // --> gives 34
// }
// {
//     let x = 14;
//     let y = "20";
//     let z = x + y;
//     console.log(z);  // --> gives 1420
// }

// {
//     var input = prompt("enter the number");
//     let a = Number.parseInt(input,2); //Converts decimal to binary i,e base 10 to base 2
//     console.log(a);
    
// }
// {
//     var input = prompt("enter the number");
//     let a = Number.parseInt(input,8); //Converts decimal to octal i,e base 10 to base 8
//     console.log(a);
    
// }
// {
//     var input = prompt("enter the number");
//     let a = Number.parseInt(input,16); //Converts decimal to hexadecimal i,e base 10 to base 16
//     console.log(a);
    
// }

// Maths methods in JavaScript

// {
//     let abs = Math.abs(-54);     //return the absolute value
//     console.log(abs);
//     let goUp = Math.ceil(0.1);   // returns the upper value
//     console.log(goUp);
//     let goDown = Math.floor(0.99);  // return the lower value
//     let round = Math.round(1.1); // returns the rounded value
//     console.log(round);
//     let round2 = Math.round(1.6); // returns the rounded value
//     console.log(round2);
//     let getInt = Math.trunc(1.33333);
//     console.log(getInt);   //return only integer part

// }


// String object

// {
//     let myName = "tulasidas";  // maName is a primitive type
//     let yourName = new String("Claire"); //yourName is object  type String

//     console.log(myName);
//     console.log(yourName);
// }
// {
//         let myName = "tulasidas";  // maName is a primitive type
        
    
//         console.log(myName[1]); // return the character at place 1 i,e u
        
//     }

// //we can also concatinate string by using the following 
// {
//     let name = "tulasidas";
//     console.log('my name is ${name}');
// }

// to know the length  of the string we use length function
// {
//     let a = "tulasidas";
//     console.log(a.length);
// }


// String methods in js 
// charAt(index) return a character at a particular index in the string
// concat("string") concatinates a string with another string
// includes("string") checks whether the string is presesnt or not in the main string return true or false
// indexOf("string") returns the index of particular string
// lastIdex("string") returns the last occurance of the string or charcter 
// substring(first index, last index) return the substring from first index to last index
// substr(from index, to index) return from index to to index(how many indexes you want)
// toUpperCase() to convert the string to upeer case
// toLowerCase() to conver the string to lower case
// trimStart() to trim the white spaces at the beginning
// trimEnd() to trim the while spaces at the end
// spilt(" ") spilt the string whenever a while space occures

// {
//     let name = "Today we will talk about strings and string methods";
//     console.log(name.charAt(2));
//     let favFood = "My fav food is";
//     console.log(favFood.concat(" chicken leg piece"));
//     let search1= "we";
//     let search2 = "tulasidas";
//     console.log(name.includes(search1));
//     console.log(name.includes(search2));
//     // inorder to search from a partcular index we have to pass index value after
//     console.log(name.includes(search1,9)); //return false because we search 'we' after index 9
//     console.log(name.indexOf("we"));
//     console.log(name.lastIndexOf("a"));
//     console.log(name.substring(6,8));
//     console.log(name.substr(6,7));
//     let myName = "TulAsIdas";
//     console.log(myName.toUpperCase());
//     console.log(myName.toLowerCase());
//     console.log(myName);   
//     let yourName = "      hello Iam tulasidas     ";
//     console.log(yourName);
//     console.log(yourName.trimStart());
//     console.log(yourName.trimEnd());
//     console.log(yourName.split(" "));// ['', '', '', '', '', '', 'hello', 'Iam', 'tulasidas', '', '', '', '', '']

// }


//  Functions and Objects
//  In the below example position is an object
// A mutable object is an object whose state can be modified after it is created.

// Immutables are the objects whose state cannot be changed once the object is created.

// Strings and Numbers are Immutable. Lets understand this with an example:
// {
//     let position = {
//         x:10,
//         y:20
//     }
//     console.log(position);
//     let myPosition = position;
//     myPosition.x = 55;
//     console.log(myPosition);
//     console.log(position);
// }

// Methods inside the objects
// {
//     let position = {
//         x:10,
//         y:20,
//         print: function(){
//             console.log(`x:${this.x}, y:${this.y}`);
//         }

//     }
//     position.print();
// }

// declaring the function outside of the object
// {
//     function print(){
//         console.log("tulasidas biradar");
//     }
//     print();  //here we are just calling the function by using just function name
// }

// we can create nested objects

// {
//     let person = {
//      myobject:{
//          name: "tulasidas",
//          age:21
//      }   
//     }
//     console.log(person.myobject.name); // inorder to access the inner object we need to use the outerobject.innerobject.property
//     console.log(person.myobject.age);
// }


//  conditional statements in JavaScript

// {
//     let name = prompt("Enter your name").toLowerCase();
//     if(name == "tulasidas"){
//         console.log("Hello "+name);
//     }else{
//         console.loog("You are not authorised");
//     }
// }

// comparision operators

// === strict equality
// !== not equal
// == equals
// >= greater than equal
// < less than
// > greater than

// Logical Opeators

// && logical and
// || logical or
// ! logical not

// switch statement

// {
//     let name = prompt("Enter your name");
//     switch(name){
//         case "tulasi":
//             console.log("welocme tulsidas");
//             break;
//         case "dikku":
//             console.log("welcome digambar");
//             break;

//         default: 
//             console.log("Bro you are not allowed");
//             break;

//     }
// }

// ternaray operator if the condition is true, expression one gets executed else expression 2 gets executed 

// {
//     let name = prompt("Enter your name");
//     let value = name=== "tulasi"?10:11;
//     console.log(value)

// }

// Intriduction to Loops

// ICU --> Initialization, C-->Condition, U--> Update
// we use while loop when we dont know how many times the loop gets executed
// it is also called indefinite loop
// {
//     let i=5;     //intitilization
//     while(i>0){       // condition
//         console.log(i);
//         i--;          //update
//     }
// }

// For loop

// we use for loop when we know how many times we want to execute the loop
// it is also  called as finite loop
// {
//     for(let i =0;/*(Intitlization)*/i<6;/*(Condition)*/i++/*(Update)*/){
//         console.log(i);
//     }
// }
// //                 Flow chart
// //                initilization
// //                 condition
// //                 statements gets executed
// //                 Update

// Do while loop
// irrespective of the conditon the first statement in the do while loop gets executed
// let i =0; 
// do{
//     console.log(i);   -->Here 0 gets printed even the condtion is false
//     i++;
// }while(i>10);

//  Break : We use Break statement whenever we want to come out of the present loop 

// {
//     let i = 5;
//     while(i>0){
//         console.log(i); 
//         if(i==3){
//             break;
//         }
//         i--;
        
//     }
// }

// Continue  : When continue statement gets executed the iterator stop executing and goes to next iterator

// {
//     for(let  i=0;i<5;i++){
//         if(i==3){         // --> here when the condititon is true the loop gets executed and continue gets executed, so the loop directly goes to next iterator without executing the next statements
//             continue;
//         }
//         console.log(i);
//     }
// }

// Introduction to arrays
// In js arrays are dynamic we can change the length of the arrays
// by doing arrayname.length = 30;
// if we try to assign a value to the index that is not there, the array itself gets exented
// In java script in arrays you can store heterogenous elements
// {
//     let array = [1,2,3,4];
//     console.log(array.length);    // return the length of the arrray
//     array.length = 7;
//     console.log(array.length);
//     console.log(array);     //[1, 2, 3, 4, empty × 3]
//     array[8] = 5;
//     console.log(array.length);
//     console.log(array)    //[1, 2, 3, 4, empty × 4, 5]
// }

// Intro to multidimentional arrays

// {
//     let grades = [               // grades is an array of array
//         [1,2,3,4],
//         [2,3,4,5],
//         [9,8,7,6,5]

//     ];
//     console.log(grades);
//     console.log(grades[0]);
//     console.log(grades[1]);    
// }

// we can also store the heterogeneous elemetns into the array
// in the below the array contains integer, string, function
// {
// let array  = [12, "tulasidas", function(){console.log("this is inside the array")},{}];
// array[2]();
// }

//  We can also crop the length of the arrays
// {
//     let arrays = [1,2,3,4,5];
//     arrays.length = 2;
//     console.log(arrays);
// }

// {
//     let arrays = [1,2,3,4,5,6,7,8];
//     arrays.length = 30;
//     arrays[34] = 9;
//     for(let i=0;i<arrays.length;i++){
//         console.log(arrays[i]);
//     }
//     for(let j=0;j<arrays.length;j++){
//         if(arrays[j]!= undefined){      //skips the undefined arrays
//             console.log(arrays[j]);
//         }
//     }
// }


// Arrays methods
// push(element) --> Inorder to insert elements into the array we use the push method
// pop() for removing or popping the element from the arrays i,e from end and it return the popped element
// unshift(element) --> for adding the element at the beginning
// shift(element) --> for removing the element from the beginning
// splice(start index, how many elements you want to delete) for removing certain elements from the array,
// it returns the deleted elements from the array
// spice(start index, how many elements you want to delete, elements you want to add)
// sort() to sort the elements based upon the places
// reverse() reverse the elements of the array
// fill(element ,start index, ending index) from start index to end index element get  inserted into the array 
// array1.concat(array2)   concatinations of two arrays, first array and second array. when we concarinate two arrays a new array is created to store the values
// push methods adds elements to the same array, concat creates a new array and elements to it
// includes(element) to check whether element is present in the array or not return true or false
// indexOf(element) to get the index of particular element
// join() to conver the array into string, but the original array remain same
// join("delimeter") by default the delimter is space
// slice(start index, end index) to get certain elements from the array

// {
//     let arrays = [];     //another way to define the array
//     while(true){
//         let input = prompt("for adding enter anything for quitting type q");
//         if(input == 'q' || input == null){
//             break;
//         }
//         arrays.push(input);

//     }
//     console.log(arrays);

// }
// push, pop, shift, unshift
// {
//     let arrays = [];
//     arrays.push(1);
//     arrays.push(2);
//     arrays.push(3);
//     arrays.push(4);
//     console.log(arrays);
//     console.log(arrays.pop());  // returns the popped element
//     console.log(arrays);
//     arrays.unshift(100);   // adds 100 in the begining of the array
//     console.log(arrays);
//     arrays.unshift(200);
//     console.log(arrays);
//     arrays.shift(); // removes the element from the beggining
//     console.log(arrays);

// }

// spice(start index, how many elements you want to delete ) return the deleted elements from the array

// {
//     let array = [1,2,3,4,6,7,5];
//     console.log(array.splice(1,3));  // --> deletes the elements [2,3,4]
//     console.log(array);
//     array.splice(1,0,100,200,300);   // splice(index, how many elements you want to delete, elements you want to add)
//     console.log(array);   //[1, 100, 200, 300, 6, 7, 5]

// }

// sort method
// {
//     let arrays = [0,0,0,20,10,1,3,55];
//     console.log(arrays.sort());   //[0, 0, 0, 1, 10, 20, 3, 55]
//     // inorder to sort the elements by actual order we need to use call back function
//     // Call back function: A function that is passed as an argument, and invoked inside
//     arrays.sort(function(a,b){
//         return a-b;   
//     });
//     console.log(arrays); //[0, 0, 0, 1, 3, 10, 20, 55]
// }

// reverse the elements the elements of the array
// {
//     let array =[1,2,3,4,5];
//     console.log(array);     //[1, 2, 3, 4, 5]
//     console.log(array.reverse());   //[5, 4, 3, 2, 1]
// }

// filling the array with a particular element
// {
//     let array = [1,2,4,5,6,7];
//     array.fill(-1,1,5);
//     console.log(array); //[1, -1, -1, -1, -1, 7] the first index is inclusive the last index is not inclusive
// }

// concatination of two arrays 

// {
//     let array1 = [1,2,3,45,5];
//     let array2 = [100,200,300,400];
//     console.log(array1.concat(array2));
//     let array3 = array1.concat(array2);
//     console.log(array3);
    
// }

// includes method
// {
//     let array = [1,2,3,4,5];
//     console.log(array.includes(1));   // returns true because 1 present in the array
//     console.log(array.includes(7));   // returns false because 1 is not present in the array
// }

// indexOf(element)
// {
//     let array = [1,2,3,4,5]; 
//     console.log(array.indexOf(1));   // return 0 because the index of the element is 0
// }


// Join method
// {
//     let array = [1,2,3,4,5]; 
//     let string = array.join();  // converting object  to string
//     console.log(string);
//     console.log(typeof(string));   // returns string
//     console.log(array);
//     console.log(typeof(array));    // returns object
// }

// slice method
// {
//     let  array = [1,2,3,4,5,6];
//     console.log(array.slice(0,2));   // first index is inclusive last index is not inclusive
// }


//  For each method for printing elements of the Arrays
// for single dimension arrays

// {
//     let grades = [1,2,3,4,5,60];
//     grades.forEach(function(element){
//         console.log(element);
//     })
// }

// for multidimentional arrays for each method
// syntax : arrayobject.forEach(function(element))
// {
//     let grades = [[1,2,3,4],[10,2,4,5],[1]];
//     grades.forEach(function(row){
//         row.forEach(function(element){
//             console.log(element);
//         })
//         console.log("\n");
//     })
// }

// Date method in JavaScript
// {
//     var valentine = new Date();
//     console.log(valentine);   //Fri Oct 15 2021 11:38:14 GMT+0530 (India Standard Time)
// }

// {
//     var date = new Date(1990,11,31);
//     console.log(date);   //return that particular day Mon Dec 31 1990 00:00:00 GMT+0530 (India Standard Time)
// }


// Functions in JavaScript
// syntax: function functionName(arguments)
// {
//     function addition(a,b){
//         return a+b;
//     }
//     console.log(addition(5,3));
// }

// // JavaScript is flexible in using functions

// {
//     function multiplication(a,b){
//         return a*b;
//     }
//     console.log(multiplication(5,6,"hello"));    // the multiplication function only takes two arguments and the reamaining argiuments gets ignored and doesn't give any error
// }

// Because of the above reason function overloading is not possible in java script
// In javascript function are treared as first class citizens. Functions are objects

// Passing a function as parameter and invoking it inside other function is known as call back function 
// we can also return a function 
// Passing arguments to a funtion

// 1.call by value  2.Call by reference
// Any changes made inside the function in call by value do not reflect outside of the function
// Any changes made inside the function in call by reference reflect  out side of the function



// Call by Value
// {
//     function fun(x){
//         x = x+1;
//         console.log(x);
//     }
//     let x = 6;                     //Here we are giving primitive type as an argument
//     fun(x);
//     console.log(x);
// }
// Call by Reference
{
    function fun(x){                         
        x.name = "tulasisdas";              //whatever changes made to the object reflect outside of the function also
    }
    let obj = {name:"dilu"};
    console.log(obj);
    fun(obj);                            // here we are passing the object as a reference
    console.log(obj)
} 





































































































































// //Polymorphism
// {
//     let user = {
//         active : true,
//         sayHello: function(){
//             return this.name+" says hello!";
//         }
//     };
//     let student = {
//         name: "tulasidas",
//         studies: "mathematics"
//     };
//     let teacher = {
//         name : "calabcurry",
//         taches: ["mathematics","siences"],
        
//         sayHello: function(){
//             let message = this.name + " teaches ";
//             this.taches.forEach(function(e){
//                 message += e +" ";
//             });
//             return message;
           
//         }
//     };
//     Object.setPrototypeOf(student, user);
//     Object.setPrototypeOf(teacher,user);
//     let newMembers = [student, teacher];
//     newMembers.forEach(function(elem){
//         console.log(elem.sayHello());

//     });
//     }













// {
//     let user = {
//         active: true
//     };
//     let student = {
//         name: "tulasidas"
//     };
//     let teacher = {
//         teaching : ["maths","computer scinece"]
//     };
//     student.active = false;
//     Object.setPrototypeOf(teacher, user);
//     Object.setPrototypeOf(student, user);
//     console.log(student.active);
// }























// {
//     function User(name,interests){              //constructor function
//         this.name = name;
//         this.interests = interests;

//     }
//     function newUser(name,interests){             //factory function contains return value
//         let obj = {
//             name: name,
//             interests: interests
//         };
//         return obj;
//     }
//     let a = new User("tulasidas",["Dancing","Singing","coocking"]);
//     let b = newUser("claire",["speaking"]);
//     console.log(a,b);
// }




















// to change the value of this 
// {
//     function tulasi(input1, input2){
    
//     console.log(input1+input2);
//     console.log(this);

// }

//     tulasi.call("tulasi",1,2);
// }
















































// {   

//     let fun = {                                    //here the this value is gives instances of object
//         name: "tulasi",
//         outPutMe: function(){
//             console.log(this);


//         }
            
//     };
//     function Person(){
//         console.log(this);
//         this.name = "tulasidas";
//         console.log(this);
//     }

//     let arrow = () =>{
//         return this;
//     }
//     // fun.outPutMe();
//     // console.log(arrow());
//     // let person = new Person();
// }









































// {
//     function pow(x,y){
//         let total=1;
//         for(let i=1;i<=y;i++){
//            total *= x;
//         }
//         return total;
//     }
//     // let arr = [pow];
//     // console.log(arr[0](3,2));
//     // let obj ={
//     //     power:pow
//     // };
//     // console.log(obj.power(4,2));
//     // pow.description="This gives the power of the number";
//     // console.log(pow.description);
//     // function callBackFunc(example){
//     //    return example;
//     // }
//     // let a = callBackFunc(pow);
//     // console.log(a(2,3));
    
// }