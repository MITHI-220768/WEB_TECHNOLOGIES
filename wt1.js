function hello(){
    alert("hello everyone")
}
function intro(){
const name="Mithilesh Kumar";
let age=20;
console.log(name);
console.log(age);
}

const username="Mithilesh Kumar";
document.getElementById("name").innerText=username;
let userplace="Andhra Pradesh";
document.getElementById("place").innerText=userplace;
const userskill=["html","css","js"];
document.getElementById("skill").innerText=userskill;
let userrole="Analyst";
document.getElementById("role").innerText=userrole;
let userexp=1;
document.getElementById("exp").innerText=userexp + " years";
function updateplace(){
    userplace="Hyderabad";
    document.getElementById("place").innerText=userplace;
    console.log(userplace);
}
function addskill() {
    let newSkill = prompt("Enter a new skill:");

    if (newSkill && !userskill.includes(newSkill)) {
        userskill.push(newSkill);
        document.getElementById("skill").innerText = userskill.join(", ");
        console.log(userskill);
    } else {
        alert("Skill already added or invalid input");
    }
}

function updaterole(){
    userrole="Senior Analyst";
    document.getElementById("role").innerText=userrole;
    console.log(userrole);
}
function updateExp(){
    userexp++;
    document.getElementById("exp").innerText=userexp + " years";
    console.log(userexp);
}