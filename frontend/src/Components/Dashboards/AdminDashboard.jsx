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
import AdminChart1 from "../AdminChart1";
import AdminChart2 from "../AdminChart2";

const AdminDashboard = ({clicked, data}) => {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[52px]');
  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
     <div className="flex bg-gray-300 lg:cols-1"> {/*gap-6 */}
      
      <div className="flex flex-col w-full h-full mb-5 px-8 gap-y-4 ">
      {/* <BreadCrumb/> */}
      {/* Stats components */}
      <div className="w-full bg-white pt-[20px]">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 sm:gap-1 lg:grid-cols-2 xl:grid-cols-4 gap-6 xl:gap-16 w-full p-3 text-white lg:mb-5" style={{backgroundSize: "cover"}}>
        {/* first compo */}
  <div class="p-2 md:p-2 rounded-md bg-blue-700 lg:h-[60%] sm:h-[75%] grid grid-cols-2 ml-2">
    <div className="flex flex-row justify-between text-2xl space-x-9 justify-items-center">
      <h1>No. CS Students</h1>
      <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>850</h1>
    </div>
    {/* <div className="pr-3 text-4xl">3.065</div> */}
	{/* <h3 class="mt-4 text-base md:text-xl font-medium text-gray-800">
	  Your feature here
	</h3> */}
  </div>
   {/* second compo */}
  <div class="p-2 md:p-2 rounded-md bg-blue-700 sm:h-[75%] lg:h-[60%] grid grid-cols-2">
	<div className="flex flex-row justify-between pb-5 text-2xl space-x-9 justify-items-center">
      <h1>No. IS Students</h1>
      <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>460</h1>
    </div>
    {/* <div className="pr-3 text-4xl">3.065</div> */}
  </div>
   {/* third compo */}
  <div class="p-2 md:p-2 rounded-md bg-blue-700 sm:h-[75%] lg:h-[60%] grid grid-cols-2 ">
	<div className="flex flex-row justify-between text-2xl space-x-9 sm:mb-10 justify-items-center">
    <h1>Registered Students</h1>
    <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>1025</h1>
    </div>
    {/* <div className="text-4xl x-4">3.065</div> */}
  </div>
   {/* fourth compo */}
  <div class="p-2 md:p-2 rounded-md bg-blue-700 sm:h-[75%] lg:h-[60%] space-x-6 grid grid-cols-2 mr-2 ">
	<div className="flex flex-row justify-between text-2xl space-x-9 sm:mb-10 justify-items-center">
      <h1>Total Courses</h1>
      <h1 className="ml-12 text-4xl font-semibold bg-cover sm:mb-6" style={{marginTop: "-6px"}}>24</h1>
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
  </div>
</div>
  );
};

export default AdminDashboard;