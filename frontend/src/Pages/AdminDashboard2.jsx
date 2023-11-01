import React, { useState } from "react";
import { HiMenuAlt3 } from "react-icons/hi";
import { MdOutlineDashboard } from "react-icons/md";
import { RiSettings4Line } from "react-icons/ri";
import { TbReportAnalytics } from "react-icons/tb";
// import { AiOutlineUser, AiOutlineHeart } from "react-icons/ai";
import { FiFolder, FiShoppingCart } from "react-icons/fi";
import { Link } from "react-router-dom";
import AdminChart1 from "../Components/AdminChart1"
import AdminChart2 from "../Components/AdminChart2"
import DashboardTable2 from "../Components/DashboardTable2";

const AdminDashboard2 = () => {
  const menus = [
    { name: "dashboard", link: "/", icon: MdOutlineDashboard },
    // { name: "MCQ", link: "/", icon: AiOutlineUser },
    // { name: "messages", link: "/", icon: FiMessageSquare },
    { name: "Subjects", link: "/", icon: TbReportAnalytics, margin: true },
    { name: "Teachers", link: "/", icon: FiFolder },
    { name: "Students", link: "/", icon: FiShoppingCart },
    // { name: "Saved", link: "/", icon: AiOutlineHeart, margin: true },
    { name: "Setting", link: "/", icon: RiSettings4Line },
  ];
  const [open, setOpen] = useState(true);
  const data = [
    {
      name: 'Page A',
      uv: 4000,
      pv: 2400,
      amt: 2400,
    },
    {
      name: 'Page B',
      uv: 3000,
      pv: 1398,
      amt: 2210,
    },
    {
      name: 'Page C',
      uv: 2000,
      pv: 9800,
      amt: 2290,
    },
    {
      name: 'Page D',
      uv: 2780,
      pv: 3908,
      amt: 2000,
    },
    {
      name: 'Page E',
      uv: 1890,
      pv: 4800,
      amt: 2181,
    },
    {
      name: 'Page F',
      uv: 2390,
      pv: 3800,
      amt: 2500,
    },
    {
      name: 'Page G',
      uv: 3490,
      pv: 4300,
      amt: 2100,
    },
  ];

  const data01 = [
    { name: 'Group A', value: 400 },
    { name: 'Group B', value: 300 },
    
  ];
  
  const data02 = [
    { name: 'Group A', value: 2400 },
    { name: 'Group B', value: 4567 },
    
  ];
  return (
    <div>
     <div className="flex bg-gray-300 lg:cols-1"> {/*gap-6 */}
      <div
        className={`bg-[#1643d6] min-h-screen ${
          open ? "w-72" : "w-16"
        } duration-500 text-gray-100 px-4`}
      >
        <div className="flex justify-end py-3">
          <HiMenuAlt3
            size={26}
            className="cursor-pointer"
            onClick={() => setOpen(!open)}
          />
        </div>
        <div className="relative flex flex-col gap-4 mt-4">
          {menus?.map((menu, i) => (
            <Link
              to={menu?.link}
              key={i}
              className={` ${
                menu?.margin && "mt-5"
              } group flex items-center text-sm  gap-3.5 font-medium p-2 hover:bg-gray-800 rounded-md`}
            >
              <div>{React.createElement(menu?.icon, { size: "20" })}</div>
              <h2
                style={{
                  transitionDelay: `${i + 3}00ms`,
                }}
                className={`whitespace-pre duration-500 ${
                  !open && "opacity-0 translate-x-28 overflow-hidden"
                }`}
              >
                {menu?.name}
              </h2>
              <h2
                className={`${
                  open && "hidden"
                } absolute left-48 bg-white font-semibold whitespace-pre text-gray-900 rounded-md drop-shadow-lg px-0 py-0 w-0 overflow-hidden group-hover:px-2 group-hover:py-1 group-hover:left-14 group-hover:duration-300 group-hover:w-fit  `}
              >
                {menu?.name}
              </h2>
            </Link>
          ))}
        </div>
      </div>
      <div className="flex flex-col w-full h-full mt-10 mb-5 ml-5 mr-5 gap-y-4 ">
      <div class=" grid-cols-1 gap-4 lg:grid-cols-3 lg:gap-8 bg-white h-auto flex justify-between rounded p-5">
  <div className="text-lg text-gray-700">
    Admin Dashboard
    <div className="text-base text-gray-500">
      Home
    </div>
  </div>
  <div className="text-base text-gray-500">
    11.30 AM
    <div className="">
      08/08/2023
    </div>
  </div>
</div>
      {/* Stats components */}
      <div className="w-full bg-white lg:pb-3">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 sm:gap-1 lg:grid-cols-2 xl:grid-cols-4 gap-6 xl:gap-16 w-full pt-3 text-white" style={{backgroundSize: "cover"}}>
        {/* first compo */}
  <div class="p-6 md:p-10 rounded-md bg-blue-700 lg:h-3/6 sm:h-3/5 grid grid-cols-2 ml-2">
    <div className="flex flex-row justify-between text-2xl space-x-9 justify-items-center">
      <h1>G.P.A.</h1>
      <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>3.065</h1>
    </div>
    {/* <div className="pr-3 text-4xl">3.065</div> */}
	{/* <h3 class="mt-4 text-base md:text-xl font-medium text-gray-800">
	  Your feature here
	</h3> */}
  </div>
   {/* second compo */}
  <div class="p-6 md:p-10 rounded-md bg-blue-700 sm:h-3/5 lg:h-3/6 grid grid-cols-2">
	<div className="flex flex-row justify-between pb-5 text-2xl space-x-9 justify-items-center">
      <h1>G.P.A.</h1>
      <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>3.065</h1>
    </div>
    {/* <div className="pr-3 text-4xl">3.065</div> */}
  </div>
   {/* third compo */}
  <div class="p-6 md:p-10 rounded-md bg-blue-700 sm:h-3/6 lg:h-3/6 grid grid-cols-2 ">
	<div className="flex flex-row justify-between text-2xl space-x-9 sm:mb-10 justify-items-center">
    <h1>G.P.A.</h1>
    <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>3.065</h1>
    </div>
    {/* <div className="text-4xl x-4">3.065</div> */}
  </div>
   {/* fourth compo */}
  <div class="p-6 md:p-10 rounded-md bg-blue-700 sm:h-3/6 lg:h-3/6 space-x-6 grid grid-cols-2 mr-2 ">
	<div className="flex flex-row justify-between text-2xl space-x-9 sm:mb-10 justify-items-center">
      <h1>G.P.A.</h1>
      <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>3.065</h1>
    </div>
    {/* <div className="pr-3 text-4xl ">3.065</div> */}
  </div>
</div>
   <div className="grid grid-cols-2 mr-2 lg:mb-7 h-1/2 lg:pr-6 ">
    <div className=" lg:w-5/6 lg:ml-16">
  <AdminChart1 />
  </div>
  <div
   className="w-auto bg-gray-300 shadow-md lg:w-5/5 lg:mb-2 sm:rounded-lg lg:mr-16 lg:pb-2" >
    <h1 className="pt-3 pb-5 font-semibold text-gray-700 ml-14">No. of papers Graded</h1>
  <AdminChart2 />
  </div>
  </div>
</div>
</div>
      {/* state background */}
      {/* <div className="m-3 text-lg font-semibold text-gray-900">
    
      </div> */}
      
      
    </div>
    </div>
  );
};

export default AdminDashboard2;
