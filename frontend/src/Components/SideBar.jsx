import classnames from 'classnames';
import { Link ,useLocation } from 'react-router-dom';
import { BsFillBookFill,BsBookmarksFill } from "react-icons/bs";
import { BiAlarmOff,BiLogOut } from "react-icons/bi";
import { MdSubject,MdSettings } from "react-icons/md";
import { IoNewspaperOutline } from "react-icons/io5";
import { TiThMenu } from "react-icons/ti";
import { HiMenuAlt2 } from "react-icons/hi";
import { CgProfile } from "react-icons/cg";
import {useState} from 'react';
import AdminSidebar from './Sidebar/AdminSidebar';  
import TeacherSidebar from './Sidebar/TeacherSidebar';
function SideBar({dashboard,subjects,markingSchemes,answerPapers,mcq,clicked,onClickFunc}) {
  //Gets details from local storage
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  const userType=allItems['user_role'];
  // console.log(userType);
  
  const currentURL = window.location.href;
  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')
  const [isClicked,setClick] = useState(false)

  const classes = classnames('flex flex-col pl-1 justify-center cursor-pointer py-3 hover:bg-white hover:bg-opacity-30 rounded rounded-lg my-2');
  const bottomclasses = classnames('flex flex-col items-center justify-center cursor-pointer py-4');
  const backGroundColor = classnames('bg-white bg-opacity-30 rounded rounded-lg');
  let navbarclasses;
  // console.log("clicked::"+clicked)
  if(clicked==="outer"){
    navbarclasses = classnames('h-full z-20 fixed px-2 text-white font-bold text-center flex flex-col justify-between sidebar w-16 bg-[#4457FF] outer pt-1')
  }else if(clicked==="inner"){
    navbarclasses = classnames('h-full z-20 fixed px-2 text-white font-bold text-center flex flex-col justify-between sidebar w-64 bg-[#4457FF] inner pt-1 max-sm:w-14')
  }

  let sidebarComponent;

  if (userType === "admin") {
    sidebarComponent = <AdminSidebar clicked={clicked} />;
  }else if (userType === "teacher") {
    sidebarComponent = <TeacherSidebar clicked={clicked} />;
  }
  //  else {
  //   sidebarComponent = <DefaultSidebar clicked={clicked} />;
  // }


  //When logout button clicked
  const handleLogout = () => {
    localStorage.removeItem('tokenData');
    window.location.href = '/';
  }


  return (
    <div className={navbarclasses}>
      <div className="text-left">
        <HiMenuAlt2 className='-ml-2 text-6xl flex flex-col cursor-pointer py-3' onClick={onClickFunc}/>
        {sidebarComponent}
      </div>
      <div className={bottomclasses}>
        <div className='w-full'>
          <Link to="/profile" className={`flex hover:bg-white hover:bg-opacity-30 rounded rounded-lg items-center w-full py-3 ${clicked === 'outer' ? 'justify-center': 'justify-right'}`}><div className='ml-1 block text-3xl pr-1'><CgProfile/></div>{clicked==="inner" ? <div className='ml-1 max-sm:hidden'>Profile</div> : ""}</Link>
          {/* <Link to="/settings" className='shadow shadow-gray-600 flex justify-center hover:bg-sky-300 w-full py-4'>{clicked==="inner" ? <div className='ml-1 max-sm:hidden'>Settings</div> : <div className='ml-1 block text-3xl pr-1'><MdSettings/></div>}{clicked==="inner" ? <div className='mr-1 max-sm:block sm:hidden text-3xl'><MdSettings/></div> : ""}</Link> */}
          <button onClick={handleLogout} className={`flex hover:bg-white hover:bg-opacity-30 rounded rounded-lg items-center w-full py-3 ${clicked === 'outer' ? 'justify-center': 'justify-right'}`}><div className='ml-1 block text-3xl pr-1'><BiLogOut/></div>{clicked==="inner" ? <div className=' ml-1 max-sm:hidden'>Logout</div> : ""}</button>
        </div>
      </div>
    </div>
  )
}

export default SideBar;
