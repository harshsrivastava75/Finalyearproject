export default function RegisterStudent(){

return(

<div className="bg-gray-800 rounded-xl p-5">

<h2 className="text-xl mb-4">

Register Student

</h2>

<input

placeholder="Student Name"

className="w-full p-3 rounded mb-3 text-black"

/>

<input

placeholder="Roll Number"

className="w-full p-3 rounded mb-3 text-black"

/>

<input

placeholder="Department"

className="w-full p-3 rounded mb-3 text-black"

/>

<button className="bg-blue-600 w-full p-3 rounded">

Save Student

</button>

</div>

)

}