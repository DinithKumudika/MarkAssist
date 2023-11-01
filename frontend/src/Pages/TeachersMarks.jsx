import React, { useState } from "react";
import { HiMenuAlt3 } from "react-icons/hi";
import { MdOutlineDashboard } from "react-icons/md";
import { RiSettings4Line } from "react-icons/ri";
import { TbReportAnalytics } from "react-icons/tb";
// import { AiOutlineUser, AiOutlineHeart } from "react-icons/ai";
import { FiFolder, FiShoppingCart } from "react-icons/fi";
import { Link } from "react-router-dom";
import DashboardTable1 from '../Components/DashboardTable1';
import DashboardTable2 from "../Components/DashboardTable2";
import TeacherMarksTable from '../Components/TeacherMarksTable'

const AdminHandleStudents2 = () => {
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
//   const data = [
//     {
//       name: 'Page A',
//       uv: 4000,
//       pv: 2400,
//       amt: 2400,
//     },
//     {
//       name: 'Page B',
//       uv: 3000,
//       pv: 1398,
//       amt: 2210,
//     },
//     {
//       name: 'Page C',
//       uv: 2000,
//       pv: 9800,
//       amt: 2290,
//     },
//     {
//       name: 'Page D',
//       uv: 2780,
//       pv: 3908,
//       amt: 2000,
//     },
//     {
//       name: 'Page E',
//       uv: 1890,
//       pv: 4800,
//       amt: 2181,
//     },
//     {
//       name: 'Page F',
//       uv: 2390,
//       pv: 3800,
//       amt: 2500,
//     },
//     {
//       name: 'Page G',
//       uv: 3490,
//       pv: 4300,
//       amt: 2100,
//     },
//   ];

  const data01 = [
    { name: 'Group A', value: 400 },
    { name: 'Group B', value: 300 },
    
  ];
  
  const data02 = [
    { name: 'Group A', value: 2400 },
    { name: 'Group B', value: 4567 },
    
  ];

  const data = [
    { id: 1, name: 'John Doe', age: 30 },
    { id: 2, name: 'Jane Doe', age: 25 },
    { id: 3, name: 'Peter Parker', age: 20 },
    { id: 4, name: 'Bruce Wayne', age: 35 },
    { id: 5, name: 'Clark Kent', age: 28 },
    { id: 6, name: 'Diana Prince', age: 500 },
    { id: 7, name: 'Barry Allen', age: 27 },
    { id: 8, name: 'Hal Jordan', age: 32 },
  ];

  const columns = [
    { id: 'id', header: 'ID' },
    { id: 'name', header: 'Name' },
    { id: 'age', header: 'Age' },
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
      {/* <div class=" grid-cols-1 gap-4 lg:grid-cols-3 lg:gap-8 bg-white h-auto flex justify-between rounded p-5">
  
  <div className="text-base text-gray-500">
    11.30 AM
    <div className="">
      08/08/2023
    </div>
  </div>
</div> */}
      {/* Stats components */}
      <div className="w-full bg-white">
      
      <div class="grid grid-cols-1 sm:grid-cols-2 sm:gap-1 lg:grid-cols-2 xl:grid-cols-1 w-full pt-3 text-white " style={{backgroundSize: "cover"}}>
        
        {/* first compo */}
  <div class="p-6 md:p-10 rounded-md lg:h-auto sm:h-auto grid grid-cols-1 ml-2 shadow-inner">
    <div className="text-lg font-semibold text-center text-slate-950">Publish all grades</div>
    <div className="font-medium text-center text-md text-slate-950">All grades will be published to the students including Grades, Marks, GPA</div>
    <div className="flex justify-center object-center mt-5">
    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-3/4 ">
  Proceed
</button>
    </div>
  </div>
</div>

<div className="text-lg font-semibold text-center text-slate-950">Configure marks</div>
        <div className="font-medium text-center text-md text-slate-950">Configure your marks, Grade, GPA</div>
   <div className="grid grid-cols-1 mr-2">
    
    <div className="flex justify-center w-5/6 ">
    {/* <div>
      <h1>Sample Table</h1>
      <TeacherMarksTable data={data} columns={columns} />
    </div> */}
    <table class="shadow-lg bg-white border-separate border-spacing-x-14 border-spacing-y-2 rounded text-center mt-5 w-5/6 justify-center">
  <tr className="h-8">
    <th class=" px-8 py-4 rounded text-center ">Mark Range</th>
    <th class="text-center px-8 py-4 rounded">Grade</th>
    <th class="text-center px-8 py-4 rounded">GPA</th>
  </tr>
  <tr className="h-8">
    <td class="border px-8 py-4 rounded bg-gray-200">0</td>
    <td class="border px-8 py-4 rounded bg-gray-200">30%</td>
    <td class="border px-8 py-4 rounded bg-gray-200">5</td>
  </tr>
  <tr className="h-8">
    <td class="border px-8 py-4 rounded bg-gray-200">0</td>
    <td class="border px-8 py-4 rounded bg-gray-200">30%</td>
    <td class="border px-8 py-4 rounded bg-gray-200">5</td>
  </tr>
  <tr className="h-8">
    <td class="border px-8 py-4 rounded bg-gray-200">0</td>
    <td class="border px-8 py-4 rounded bg-gray-200">30%</td>
    <td class="border px-8 py-4 rounded bg-gray-200">5</td>
  </tr>
  <tr className="h-8">
    <td class="border px-8 py-4 rounded bg-gray-200">0</td>
    <td class="border px-8 py-4 rounded bg-gray-200">30%</td>
    <td class="border px-8 py-4 rounded bg-gray-200">5</td>
  </tr>
  <tr className="h-8">
    <td class="border px-8 py-4 rounded bg-gray-200">0</td>
    <td class="border px-8 py-4 rounded bg-gray-200">30%</td>
    <td class="border px-8 py-4 rounded bg-gray-200">5</td>
  </tr>
  <tr className="h-8">
    <td class="border px-8 py-4 rounded bg-gray-200">0</td>
    <td class="border px-8 py-4 rounded bg-gray-200">30%</td>
    <td class="border px-8 py-4 rounded bg-gray-200">5</td>
  </tr>
</table>
  </div>

  </div>
</div>
</div>
      
    </div>
    </div>
  );
};

export default AdminHandleStudents2;
