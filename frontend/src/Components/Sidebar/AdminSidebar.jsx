import { MdSubject,MdSettings } from "react-icons/md";
import { IoNewspaperOutline ,IoStatsChart } from "react-icons/io5";
import { GiTeacher } from "react-icons/gi";
import classnames from 'classnames';
import { Link ,useLocation } from 'react-router-dom';
function AdminSidebar({clicked}) {
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  if(allItems){
    const userType = allItems['user_role'];
    if(userType!=="admin"){
      window.location.href="/";
    }
  }else{
    window.location.href="/";
  }
  const user_id=allItems['user_id'];
  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')
  const classes = classnames('flex flex-col pl-1 justify-center cursor-pointer py-3 hover:bg-white hover:bg-opacity-30 rounded rounded-lg my-2');
  const backGroundColor = classnames('bg-white bg-opacity-30 rounded rounded-lg');
  return (
    <div>
      <div className={`${classes} ${clicked === "outer" ? 'items-center': ""} ${pathName[1] === "dashboard" ? backGroundColor : ""}`}><Link to="/admin/dashboard" className='flex gap-4 items-center'><div className={`${clicked==="outer" ? ' ml-0 ' : ' ml-4 '} block text-3xl pr-1 max-sm:ml-1`}><img className="w-6" src="http://localhost:3000/chartsquare.svg" alt="logot" /></div>{clicked==="inner" ? <div className='max-sm:hidden'>Dashboard</div> :""}</Link></div>
        <div className={`${classes} ${clicked === "outer" ? 'items-center': ""} ${pathName[0] === "subjects" ? backGroundColor : ""}`}><Link to="/subjects" className='flex gap-4 items-center'><div className={`${clicked==="outer" ? ' ml-0 ' : ' ml-4 '} block text-3xl pr-1 max-sm:ml-1`}><img className="w-6" src="http://localhost:3000/cards.svg" alt="logot" /></div>{clicked==="inner" ? <div className='max-sm:hidden'>Subjects</div> : ""}</Link></div>
        <div className={`${classes} ${clicked === "outer" ? 'items-center': ""} ${pathName[1] === "teachers" ? backGroundColor : ""}`}><Link to="/admin/teachers" className='flex gap-4 items-center'><div className={`${clicked==="outer" ? ' ml-0 ' : ' ml-4 '} block text-3xl pr-1 max-sm:ml-1`}><img className="w-6" src="http://localhost:3000/Classroom.png" alt="logot" /></div>{clicked==="inner" ? <div className='max-sm:hidden'>Teachers</div> : ""}</Link></div>
        <div className={`${classes} ${clicked === "outer" ? 'items-center': ""} ${pathName[1] === "grades" ? backGroundColor : ""}`}><Link to="/admin/grades" className='flex gap-4 items-center'><div className={`${clicked==="outer" ? ' ml-0 ' : ' ml-4 '} block text-3xl pr-1 max-sm:ml-1`}><img className="w-6" src="http://localhost:3000/cards.svg" alt="logot" /></div>{clicked==="inner" ? <div className='max-sm:hidden'>Grades</div> : ""}</Link></div>
      {/* <div className={`${classes} ${clicked === "outer" ? 'items-center': ""} ${pathName[1] === "teachers" ? backGroundColor : ""}`}><Link to="/admin/teachers" className='flex items-center'><div className='ml-1 block text-3xl pr-1'><GiTeacher/></div>{clicked==="inner" ? <div className='ml-1 max-sm:hidden'>Teachers</div> : ""}</Link></div> */}
    </div>
  )
}

export default AdminSidebar
