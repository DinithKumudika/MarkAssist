import React, { useState } from "react";
import { HiMenuAlt3 } from "react-icons/hi";
import { MdOutlineDashboard } from "react-icons/md";
import { RiSettings4Line } from "react-icons/ri";
import { TbReportAnalytics } from "react-icons/tb";
// import { AiOutlineUser, AiOutlineHeart } from "react-icons/ai";
import { FiFolder, FiShoppingCart } from "react-icons/fi";
import { Link } from "react-router-dom";
import TeacherChart from '../Components/TeacherChart';
import TeacherDiscription from "../Components/TeacherDiscription";
import SubjectsDropdown from "../Components/SubjectsDropdown";
import YearsDropdown from "../Components/YearsDropdown"

const AdminHandleTeacher2 = () => {
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
    Student Dashboard
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
      <div className="w-full bg-white">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 sm:gap-1 lg:grid-cols-2 xl:grid-cols-4 gap-6 xl:gap-16 w-full pt-3 text-white lg:mb-5" style={{backgroundSize: "cover"}}>
        {/* first compo */}
  <div class="relative p-6 md:p-10 rounded-md bg-blue-700 lg:h-3/6 sm:h-3/4 grid grid-cols-2 ml-2 ">
    <div className="absolute flex flex-row w-full pr-3 lg:mb-4 lg:pl-3 mx:pt-5 space-x-14 sm:mb-4 lg:mt-4">
      <h1 className=" text-md">Non Editing Subject</h1>
      <h1 className="ml-12 text-5xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-1px"}}>02</h1>
    </div>
  </div>
  
   {/* second compo */}
  <div class="relative p-6 md:p-10 rounded-md bg-blue-700 sm:h-3/4 lg:h-3/6 grid grid-cols-2 sm:mr-2">
	<div className="absolute flex flex-row justify-between pb-5 space-x-9 justify-items-center sm:mt-2 lg:mt-5">
      <h1 className="lg:pr-10 lg:pl-3 text-md">Editing Subject</h1>
      <h1 className="ml-12 text-5xl font-semibold bg-cover sm:mb-6 lg:pr-3" style={{marginTop: "-2px"}}>03</h1>
    </div>
    
  </div>
  
   {/* third compo */}
  <div class="grid grid-cols-1 gap-4 lg:grid-cols-3 lg:gap-14 w-full lg:col-span-2 lg:mr-5 lg:pr-3">
  <div class="h-full lg:col-span-2 grid-flow-row-2 divide-y-1 divide-solid bg-white border-2 border-gray-400 border-solid rounded-md ">
    <div className="text-xl font-bold text-center h-1/2 text-violet-950">Subject</div>
    
    <div className=" h-1/2">
    <SubjectsDropdown />
    </div>
  </div>
  
  <div class="h-full rounded-md divide-y-1 border-2 border-gray-400 border-solid bg-white">
  <div className="text-xl font-bold text-center h-1/2 text-violet-950">Year</div>
    <div className=" h-1/2">
    <YearsDropdown />
    </div>
  </div>
  </div>
   
</div>
   <div className="grid grid-cols-2 mr-2">
    <div className="w-auto mb-3 ml-4 rounded bg-slate-300">
      <h1 className="pt-3 pb-5 font-semibold text-gray-600 ml-14">Overall Subject Analysis - IS 1107</h1>
  <TeacherChart />
  </div>
  <div
   className="w-auto h-auto" >
  <TeacherDiscription />
  </div>
  </div>
</div>
</div>

    </div>
    </div>
  );
};

export default AdminHandleTeacher2;
