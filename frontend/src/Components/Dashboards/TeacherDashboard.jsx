import React, { useState } from "react";
import { HiMenuAlt3 } from "react-icons/hi";
import { MdOutlineDashboard } from "react-icons/md";
import { RiSettings4Line } from "react-icons/ri";
import { TbReportAnalytics } from "react-icons/tb";
// import { AiOutlineUser, AiOutlineHeart } from "react-icons/ai";
import { FiFolder, FiShoppingCart } from "react-icons/fi";
import { Link } from "react-router-dom";
import TeacherChart from '../TeacherChart';
import TeacherDiscription from "../TeacherDiscription";
import SubjectsDropdown from "../SubjectsDropdown";
import YearsDropdown from "../YearsDropdown"
import classnames from "classnames";
import BreadCrumb from "../BreadCrumb";

const TeacherDashboard = ({clicked, data}) => {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[52px]');
  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
     <div className="flex bg-gray-300 lg:cols-1"> {/*gap-6 */}
      
      <div className="flex flex-col w-full h-full mb-5 px-8 gap-y-4 ">
      {/* <BreadCrumb/> */}
      <div className="w-full bg-white pt-[60px]">
      {/* Stats components */}
      
      <div class="grid grid-cols-1 sm:grid-cols-2 sm:gap-1 lg:grid-cols-2 xl:grid-cols-4 gap-6 xl:gap-16 w-full p-3 text-white lg:mb-5" style={{backgroundSize: "cover"}}>
        {/* first compo */}
  <div class="relative p-6 md:p-10 rounded-md bg-blue-700 lg:h-3/6 sm:h-3/4 flex flex-row justify-center items-center ">
    <div className="absolute flex flex-row justify-center items-center w-full">
      <div className=" text-md">Lecturing Subjects</div>
      <div className="text-4xl font-semibold ml-6">04</div>
    </div>
  </div>
  
   {/* second compo */}
  <div class="relative p-6 md:p-10 rounded-md bg-blue-700 sm:h-3/4 lg:h-3/6 flex flex-row justify-center items-center">
    <div className="absolute flex flex-row justify-center items-center w-full">
      <div className=" text-md">Total no. students</div>
      <div className="text-4xl font-semibold ml-6">08</div>
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

export default TeacherDashboard;