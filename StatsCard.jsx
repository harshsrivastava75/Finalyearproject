export default function StatsCard({title,value}){

return(

<div className="bg-gray-800 p-5 rounded-xl">

<h3 className="text-gray-400">

{title}

</h3>

<h1 className="text-4xl font-bold">

{value}

</h1>

</div>

)

}