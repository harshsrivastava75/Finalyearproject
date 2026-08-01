const students=[

{

name:"John",

roll:"101",

status:"Present"

},

{

name:"Emma",

roll:"102",

status:"Absent"

},

{

name:"Alex",

roll:"103",

status:"Present"

}

]

export default function AttendanceTable(){

return(

<div className="bg-gray-800 rounded-xl p-5">

<h2 className="text-2xl mb-5">

Today's Attendance

</h2>

<table className="w-full">

<thead>

<tr>

<th>Name</th>

<th>Roll</th>

<th>Status</th>

</tr>

</thead>

<tbody>

{

students.map((s,i)=>

<tr key={i}>

<td>{s.name}</td>

<td>{s.roll}</td>

<td>

<span className={`px-3 py-1 rounded ${
s.status==="Present"
?"bg-green-500"
:"bg-red-500"
}`}>

{s.status}

</span>

</td>

</tr>

)

}

</tbody>

</table>

</div>

)

}