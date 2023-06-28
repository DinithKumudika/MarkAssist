import {Link, useLocation} from 'react-router-dom';
import { MdEdit } from "react-icons/md";
function SubjectBox({subjectName,subjectCode,year,onClick,userType}) {
  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')
  // console.log("Hello::"+userType);
  var formattedString="";
  if(year){
    formattedString = year;
  }else{
    formattedString = `${subjectCode}-${subjectName}`;
  }
  return (
    <div className='h-24 w-56 mr-6 mb-8 rounded-lg z-20'>
      <div className='h-14 rounded-t-lg bg-[#4457FF] flex justify-end pr-2 pt-2 z-20' >{userType==="admin" ? <MdEdit onClick={onClick} className='text-white hover:text-black z-30 w-6 h-6 hover:bg-blue-300 rounded-lg'/> : ""}</div>
      <div className= 'w-56 text-sm p-2 bg-[#D9D9D9] rounded-b-lg'>
      {formattedString}
      </div>
    </div>
  )
}

export default SubjectBox
