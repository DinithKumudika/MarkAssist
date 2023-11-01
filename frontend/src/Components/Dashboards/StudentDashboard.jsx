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
import DashboardTable1 from '../DashboardTable1';
import DashboardTable2 from "../DashboardTable2";

const StudentDashboard = ({clicked, data}) => {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[52px]');
  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
     <div className="flex bg-gray-300 lg:cols-1"> {/*gap-6 */}
      
      <div className="flex flex-col w-full h-full mb-5 px-8 gap-y-4 ">
      {/* <BreadCrumb/> */}
      {/* Stats components */}
      <div className="w-full bg-white pt-[20px]">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 sm:gap-1 lg:grid-cols-2 xl:grid-cols-4 gap-6 xl:gap-16 w-full p-3 text-white lg:mb-1" style={{backgroundSize: "cover"}}>
        {/* first compo */}
        <div class="p-6 md:p-10 rounded-md bg-blue-700 lg:h-3/6 sm:h-3/5 grid grid-cols-2 ml-2">
    <div className="flex flex-row justify-between text-2xl space-x-9 justify-items-center">
      <h1>G.P.A.</h1>
      <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>3.065</h1>
    </div>
    
  </div>
   {/* second compo */}
  <div class="p-6 md:p-10 rounded-md bg-blue-700 sm:h-3/5 lg:h-3/6 grid grid-cols-2">
	<div className="flex flex-row justify-between pb-5 text-2xl space-x-9 justify-items-center">
      <h1>G.P.A.</h1>
      <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>2.89</h1>
    </div>
  </div>
   {/* third compo */}
  <div class="p-6 md:p-10 rounded-md bg-blue-700 sm:h-3/6 lg:h-3/6 grid grid-cols-2 ">
	<div className="flex flex-row justify-between text-2xl space-x-9 sm:mb-10 justify-items-center">
    <h1>G.P.A.</h1>
    <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>3.65</h1>
    </div>
    {/* <div className="text-4xl x-4">3.065</div> */}
  </div>
   {/* fourth compo */}
  <div class="p-6 md:p-10 rounded-md bg-blue-700 sm:h-3/6 lg:h-3/6 space-x-6 grid grid-cols-2 mr-2 ">
	<div className="flex flex-row justify-between text-2xl space-x-9 sm:mb-10 justify-items-center">
      <h1>G.P.A.</h1>
      <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>3.265</h1>
    </div>
    
  </div>
</div>
   <div className="grid grid-cols-2 mr-2">
    
    <div className="w-auto ">
  <DashboardTable1 />
  </div>
  <div
   className="w-auto " >
  <DashboardTable2 />
  </div>
  </div>
</div>
</div>

    </div>
    </div>
  );
};

export default StudentDashboard;