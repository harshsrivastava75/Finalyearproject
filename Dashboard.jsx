import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatsCard from "../components/StatsCard";
import Camera from "../components/Camera";
import AttendanceTable from "../components/AttendanceTable";
import RegisterStudent from "../components/RegisterStudent";

export default function Dashboard(){

return(

<div className="flex bg-gray-900 min-h-screen text-white">

<Sidebar/>

<div className="flex-1">

<Navbar/>

<div className="grid grid-cols-3 gap-5 p-5">

<StatsCard title="Students" value="520"/>

<StatsCard title="Present" value="486"/>

<StatsCard title="Absent" value="34"/>

</div>

<div className="grid md:grid-cols-2 gap-6 p-5">

<Camera/>

<RegisterStudent/>

</div>

<div className="p-5">

<AttendanceTable/>

</div>

</div>

</div>

)

}