import { AiOutlineMenu } from "react-icons/ai";
import classnames from 'classnames';
import Logo from '../photos/logo.png'
function NavBar({white,black,onClickFunc,clicked}) {
    const classes = classnames('text-3xl cursor-pointer',{
        'text-white':white,
        'text-black':black
    });
    // console.log("Data::",localStorage['tokenData'].firstName)
    const allItems = JSON.parse(localStorage.getItem('tokenData'));
  return (
    
    <nav className={`mb-6 z-10 bg-white fixed flex items-center justify-between shadow shadow-gray-500 h-[52px] py-3 px-4 ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:ml-16 max-sm:w-[calc(100vw-16px)]`}>
        {/* <AiOutlineMenu className={classes} onClick={onClickFunc}/> */}
        <img className='w-52' src={Logo} alt="Logo"/>
        <div className="flex gap-2 items-center">
          <div className="flex gap-2 items-center">
            <h2 className="font-bold opacity-50">{allItems.firstName} {allItems.lastName}</h2>
            <img className=" w-8" src="http://localhost:3000/profilecircle.svg" alt=""/>
          </div>
          <div className="">
            <img className=" w-8"  src="http://localhost:3000/notification.svg" alt=""/>
          </div>
        </div>
    </nav>
  )
}

export default NavBar
