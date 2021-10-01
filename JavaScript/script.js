const person = {
    firstName:"randika",
    lastName:"chathuranga",
    get fullName(){
        return (`${person.firstName} ${person.lastName}`);
    },

    set fullName(value){
        const parts = value.split(' ');
        this.firstName = parts[0];
        this.lastName = parts[1];
    }
}

person.fullName = "nuwan abe";

console.log(person.fullName);


const jobs = [
    {id:1 , isActive:true},
    {id:2 , isActive:true},
    {id:3 , isActive:false}
]

const activeJobs = jobs.filter(function(job){return job.isActive});
console.log(activeJobs);


const colors = ['red','green','yellow'];
const items = colors.map(function(color){
    return '<li>' + color + '</li>'
})

console.log(items);






// class 
class Man {
    constructor(name){
        this.name = name;
    }

    walk(){
        console.log("walk");
    }
}

const person1 = new Man("randika");
console.log(person1.name);



//inheritance
class Teacher extends Man  {
    constructor(name,age){
        super(name);
        this.age = age;
    }

    walk(){
        console.log("walk");
    }
}

const teacher = new Teacher('chathuranga',24);
console.log(teacher.age);