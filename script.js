const video = document.getElementById("video");

async function startCamera(){

    try{

        const stream = await navigator.mediaDevices.getUserMedia({
            video:true
        });

        video.srcObject = stream;

    }

    catch(error){

        alert("Unable to access camera.");

    }

}

// Example attendance data

const attendance = [

{
id:101,
name:"John",
time:"09:01 AM",
status:"Present"
},

{
id:102,
name:"Emma",
time:"09:03 AM",
status:"Present"
},

{
id:103,
name:"David",
time:"09:06 AM",
status:"Present"
}

];

const table = document.getElementById("attendanceTable");

attendance.forEach(student=>{

table.innerHTML += `

<tr>

<td>${student.id}</td>

<td>${student.name}</td>

<td>${student.time}</td>

<td>${student.status}</td>

</tr>

`;

});