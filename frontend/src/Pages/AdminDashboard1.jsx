import React from 'react'
import AdminSidebar1 from '../Components/Sidebar/AdminSidebar'

function AdminDashboard1() {
  return (
    <div>
      <AdminSidebar1 />
    </div>
  )
}

export default AdminDashboard1


// import React from 'react'
// import NavBar from '../Components/NavBar'
// import Subjects from '../Components/Subjects/Subjects'
// import {useState} from 'react'
// import SideBar from '../Components/SideBar'
// import AdminSidebar from '../Components/Sidebar/AdminSidebar'
// function AdminDashboard1() {

//   const [isClicked,setClick] = useState("outer")

//   //Function to handle the click of the hamburger menu
//   const handleClick = () => {
//     if(isClicked==="outer"){
//     setClick("inner")
//     }else{
//     setClick("outer")
//     }
//     // console.log(isClicked)
//   }

//   return (
//     <div>
        
//       <NavBar />
//       {/* <SideBar /> */}
//       <AdminSidebar dashboard subjects clicked={isClicked} onClickFunc={handleClick}/>
//       <Subjects clicked={isClicked}/>
//     </div>
//   )
// }

// export default AdminDashboard1
