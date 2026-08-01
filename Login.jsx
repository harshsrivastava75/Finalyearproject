import { useNavigate } from "react-router-dom";

export default function Login() {

const navigate=useNavigate();

return (

<div className="flex items-center justify-center h-screen bg-gray-900">

<div className="bg-gray-800 p-8 rounded-xl w-96 shadow-lg">

<h1 className="text-3xl text-white font-bold text-center mb-6">
AI Attendance
</h1>

<input
type="email"
placeholder="Email"
className="w-full p-3 rounded mb-4"
/>

<input
type="password"
placeholder="Password"
className="w-full p-3 rounded mb-4"
/>

<button
onClick={()=>navigate("/dashboard")}
className="bg-blue-600 w-full p-3 rounded text-white font-bold"
>
Login
</button>

</div>

</div>

);

}