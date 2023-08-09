import {Link, useLocation} from 'react-router-dom';
import { MdEdit } from "react-icons/md";
function SubjectBox({subjectName,subject,subjectCode,backgroundUrl,year,onClick,userType}) {
  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')
  // console.log("Hello::"+userType);
  var formattedString="";
  // if(year){
  //   formattedString = ()=>{
  //     return `<h2 className='font-bold opacity-80 text-base'>${subject.subjectCode} - ${subject.year}</h2>`;
  //   }
  // }else{
  //   formattedString = ()=>{
  //     return (`<h2 className='font-bold opacity-80 text-base'>${subject.subjectCode} - ${subject.subjectName}</h2>
  //     <h2 className='text-sm opacity-70'>Year ${subject.academicYear} > Semester ${subject.semester}</h2>`)
  //   }
  // }
  return (
    <div className='h-24 w-80 mr-6 mb-8 rounded-lg z-20'>
      <div className="h-24 rounded-t-lg flex shrink-0  z-20" >{userType && userType==="admin" ? <MdEdit onClick={onClick} className='text-white hover:text-black z-30 w-6 h-6 hover:bg-blue-300 rounded-lg'/> : ""}
        <img className='object-cover w-full rounded-t-lg ' src={`http://localhost:3000/uploads/${backgroundUrl}.png`} alt=""/>
      </div>
      <div className= 'w-80 h-16 text-sm p-2 pl-6 bg-[#D9D9D9] rounded-b-lg'>      
      {year ? <div><h2 className='font-bold opacity-80 mt-3 text-base'>{subject.subjectCode} - {subject.year}</h2></div> : (
        <div>
          <h2 className='font-bold opacity-80 text-base'>{subject.subjectCode} - {subject.subjectName}</h2>
          <h2 className='text-sm opacity-70'>Year {subject.academicYear} &gt; Semester {subject.semester}</h2>  
        </div>
        )}
      </div>
    </div>
  )
}

export default SubjectBox
