import React from 'react'
import Table1Row from './Table1Row'
import Table1Heading from './Table1Heading'

function Table1() {
  return (
    <div>
    <div className="static w-5/6 h-full pt-0 pb-4 pl-4 pr-4 mt-0 mb-2 ml-40 bg-gray-300">
      <Table1Heading />
      <Table1Row />
      <Table1Row />
      <Table1Row />
      <Table1Row />
      <Table1Row />
      <Table1Row />
      <Table1Row />
    </div>
    </div>
  )
}

export default Table1





// import { MagnifyingGlassIcon } from "@heroicons/react/24/outline";
// import { PencilIcon, UserPlusIcon } from "@heroicons/react/24/solid";
// import {
//   Card,
//   CardHeader,
//   Input,
//   Typography,
//   Button,
//   CardBody,
//   Chip,
//   CardFooter,
//   Tabs,
//   TabsHeader,
//   Tab,
//   Avatar,
//   IconButton,
//   Tooltip,
// } from "@material-tailwind/react";
 
// const TABS = [
//   {
//     label: "All",
//     value: "all",
//   },
//   {
//     label: "Monitored",
//     value: "monitored",
//   },
//   {
//     label: "Unmonitored",
//     value: "unmonitored",
//   },
// ];
 
// const TABLE_HEAD = ["Member", "Function", "Status", "Employed", ""];
 
// const TABLE_ROWS = [
//   {
//     img: "https://demos.creative-tim.com/test/corporate-ui-dashboard/assets/img/team-3.jpg",
//     name: "John Michael",
//     email: "john@creative-tim.com",
//     job: "Manager",
//     org: "Organization",
//     online: true,
//     date: "23/04/18",
//   },
//   {
//     img: "https://demos.creative-tim.com/test/corporate-ui-dashboard/assets/img/team-2.jpg",
//     name: "Alexa Liras",
//     email: "alexa@creative-tim.com",
//     job: "Programator",
//     org: "Developer",
//     online: false,
//     date: "23/04/18",
//   },
//   {
//     img: "https://demos.creative-tim.com/test/corporate-ui-dashboard/assets/img/team-1.jpg",
//     name: "Laurent Perrier",
//     email: "laurent@creative-tim.com",
//     job: "Executive",
//     org: "Projects",
//     online: false,
//     date: "19/09/17",
//   },
//   {
//     img: "https://demos.creative-tim.com/test/corporate-ui-dashboard/assets/img/team-4.jpg",
//     name: "Michael Levi",
//     email: "michael@creative-tim.com",
//     job: "Programator",
//     org: "Developer",
//     online: true,
//     date: "24/12/08",
//   },
//   {
//     img: "https://demos.creative-tim.com/test/corporate-ui-dashboard/assets/img/team-5.jpg",
//     name: "Richard Gran",
//     email: "richard@creative-tim.com",
//     job: "Manager",
//     org: "Executive",
//     online: false,
//     date: "04/10/21",
//   },
// ];
 
// export default function Example() {
//   return (
//     <Card className="w-2/3 h-2/3">
//       <CardHeader floated={false} shadow={false} className="rounded-none">
//         <div className="flex items-center justify-between gap-8 mb-8">
//           <div>
//             {/* <Typography variant="h5" color="blue-gray">
//               Members list
//             </Typography> */}
//             {/* <Typography color="gray" className="mt-1 font-normal">
//               See information about all members
//             </Typography> */}
//           </div>
          // <div className="flex flex-col gap-2 bg-blue-600 shrink-0 sm:flex-row">
          //    <Button variant="outlined" color="blue-gray" size="sm" >
          //     Add a Person
          //   </Button> 
          //   <Button className="flex items-center gap-3" color="blue" size="sm">
          //     <UserPlusIcon strokeWidth={2} className="w-4 h-4" /> Add member
          //   </Button>
          // </div>
//         </div>
//         <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
//           <Tabs value="all" className="w-full bg-gray-700 md:w-max">
//             <TabsHeader>
//               {TABS.map(({ label, value }) => (
//                 <Tab key={value} value={value}>
//                   &nbsp;&nbsp;{label}&nbsp;&nbsp;
//                 </Tab>
//               ))}
//             </TabsHeader>
//           </Tabs>
          
// <form class="flex items-center mb-3">   
//     <label for="simple-search" class="sr-only">Search</label>
//     <div class="relative w-full">
//         <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
//             <svg aria-hidden="true" class="w-5 h-5 text-gray-100 dark:text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path></svg>
//         </div>
//         <input type="text" id="simple-search" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-300 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search" required />
//     </div>
//     <button type="submit" class="p-2.5 ml-0 text-sm font-medium text-white bg-blue-700 rounded-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
//         <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
//         <span class="sr-only">Search</span>
//     </button>
// </form>

//         </div>
//       </CardHeader>
//       <CardBody className="px-0 overflow-scroll">
//         <table className="w-full ta2/3 ble-auto t-ext-left hmt-6 min-w-max">
//           <thead>
//             <tr>
//               {TABLE_HEAD.map((head) => (
//                 <th key={head} className="p-4 border-y border-blue-gray-100 bg-blue-gray-50/50">
//                   <Typography
//                     variant="small"
//                     color="blue-gray"
//                     className="font-normal leading-none opacity-70"
//                   >
//                     {head}
//                   </Typography>
//                 </th>
//               ))}
//             </tr>
//           </thead>
//           <tbody>
//             {TABLE_ROWS.map(({ name, email, job, org, online, date }, index) => {
//               const isLast = index === TABLE_ROWS.length - 1;
//               const classes = isLast ? "p-4" : "p-4 border-b border-blue-gray-50";
 
//               return (
//                 <tr key={name}>
//                   <td className={classes}>
//                     <div className="flex items-center gap-3">
//                       {/* <Avatar src={img} alt={name} size="sm" /> */}
//                       <div className="flex flex-col">
//                         <Typography variant="small" color="blue-gray" className="font-normal">
//                           {name}
//                         </Typography>
//                         {/* <Typography
//                           variant="small"
//                           color="blue-gray"
//                           className="font-normal opacity-70"
//                         >
//                           {email}
//                         </Typography> */}
//                       </div>
//                     </div>
//                   </td>
//                   <td className={classes}>
//                     <div className="flex flex-col">
//                       {/* <Typography variant="small" color="blue-gray" className="font-normal">
//                         {job}
//                       </Typography> */}
//                       <Typography
//                         variant="small"
//                         color="blue-gray"
//                         className="font-normal opacity-70"
//                       >
//                         {org}
//                       </Typography>
//                     </div>
//                   </td>
//                   <td className={classes}>
//                     <div className="w-max">
//                       <Chip
//                         variant="ghost"
//                         size="sm"
//                         value={online ? "online" : "offline"}
//                         color={online ? "green" : "blue-gray"}
//                       />
//                     </div>
//                   </td>
//                   <td className={classes}>
//                     <Typography variant="small" color="blue-gray" className="font-normal">
//                       {date}
//                     </Typography>
//                   </td>
//                   <td className={classes}>
//                     <Tooltip content="Edit User">
//                       <IconButton variant="text" color="blue-gray">
//                         <PencilIcon className="w-4 h-4" />
//                       </IconButton>
//                     </Tooltip>
//                   </td>
//                 </tr>
//               );
//             })}
//           </tbody>
//         </table>
//       </CardBody>
//       <CardFooter className="flex items-center justify-between p-4 border-t border-blue-gray-50">
//         <Typography variant="small" color="blue-gray" className="font-normal">
//           Page 1 of 10
//         </Typography>
//         <div className="flex gap-2">
//           <Button variant="outlined" color="blue-gray" size="sm">
//             Previous
//           </Button>
//           <Button variant="outlined" color="blue-gray" size="sm">
//             Next
//           </Button>
//         </div>
//       </CardFooter>
//     </Card>
//   );
// }