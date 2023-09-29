import { MdSubject,MdSettings } from "react-icons/md";
import { BsFillBookFill,BsBookmarksFill } from "react-icons/bs";
import { BiAlarmOff,BiLogOut } from "react-icons/bi";
import { IoNewspaperOutline ,IoStatsChart } from "react-icons/io5";
import classnames from 'classnames';
import { Link ,useLocation } from 'react-router-dom';
function TeacherSidebar({clicked}) {
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  // console.log(allItems);
  if(allItems){
    const userType = allItems['user_role'];
    if(userType!=="teacher"){
      window.location.href="/";
      // console.log("error");
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
        <div className={`${classes} ${clicked === "outer" ? 'items-center': ""} ${pathName[1] === "dashboard" ? backGroundColor : ""}`}><Link to="/teacher/dashboard" className='flex gap-4 items-center'><div className={`${clicked==="outer" ? ' ml-0 ' : ' ml-4 '} block text-3xl pr-1 max-sm:ml-1`}><img className="w-6" src="http://localhost:3000/chartsquare.svg" alt="logot" /></div>{clicked==="inner" ? <div className='max-sm:hidden'>Dashboard</div> :""}</Link></div>
        <div className={`${classes} ${clicked === "outer" ? 'items-center': ""} ${pathName[0] === "subjects" ? backGroundColor : ""}`}><Link to="/subjects" className='flex gap-4 items-center'><div className={`${clicked==="outer" ? ' ml-0 ' : ' ml-4 '} block text-3xl pr-1 max-sm:ml-1`}><img className="w-6" src="http://localhost:3000/cards.svg" alt="logot" /></div>{clicked==="inner" ? <div className='max-sm:hidden'>Subjects</div> : ""}</Link></div>
        <div className={`${classes} ${clicked === 'outer' ? 'items-center': ""} ${pathName[0] === "markingschemes" ? backGroundColor : ""}`}><Link to="/markingschemes" className='flex gap-4 items-center'><div className={`${clicked==="outer" ? ' ml-0 ' : ' ml-4 '} block text-3xl pr-1 max-sm:ml-1`}><img className="w-5" src="http://localhost:3000/bookmark.svg" alt="logot" /></div>{clicked==="inner" ? <div className='max-sm:hidden'>Marking Schemes</div> : ""}</Link></div>
        <div className={`${classes} ${clicked === 'outer' ? 'items-center': ""} ${pathName[0] === "answersheets" ? backGroundColor : ""}`}><Link to="/answersheets" className='flex gap-4 items-center'><div className={`${clicked==="outer" ? ' ml-0 ' : ' ml-4 '} block text-3xl pr-1 max-sm:ml-1`}><img className="w-6" src="http://localhost:3000/note-alt.svg" alt="logot" /></div>{clicked==="inner" ?  <div className='max-sm:hidden'>Answer Sheets</div> : ""}</Link></div>
        <div className={`${classes} ${clicked === 'outer' ? 'items-center': ""} ${pathName[0] === "mcq" ? backGroundColor : ""}`}><Link to="/mcq" className='flex gap-4 items-center'><div className={`${clicked==="outer" ? ' ml-0 ' : ' ml-4 '} block text-3xl pr-1 max-sm:ml-1`}><img className="w-6" src="http://localhost:3000/mcq.svg" alt="logot"/></div>{clicked==="inner" ? <div className='max-sm:hidden'>MCQ</div> : ""}</Link></div>
    </div>
  )
}

export default TeacherSidebar
