import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import MarkingSchemeConfigure from '../Components/MarkingSchemes/MarkingSchemeConfigure'
import {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom'
import axios from 'axios'
function MarkingSchemeConfigurePage() {
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  // console.log(allItems);
  if(!allItems){
    window.location.href="/";
  }
  const {markingschemeId,subjectId} = useParams();
  const user_id=allItems['user_id'];
  const [isClicked,setClick] = useState("inner");
  const [markings,setMarkings] = useState([]);

  useEffect(()=>{
    // console.log("DATA:");
    fetchMarkings();
  },[]);

  const fetchMarkings = async () =>{
    axios
    // .get(`/markings/questions?scheme=${markingschemeId}`)
    .get(`/markings/questions?sub=${subjectId}`).then((response) => {
      const data = response.data
      setMarkings(data)
      // console.log("Markings:",data)
      // Process the response data or update your React component state
    })
    .catch((error) => {
      console.error(error);
      setMarkings(null)
      // Handle the error, e.g., display an error message to the user
    });
  }
  // console.log("Marking scheme:",markings)


  // //Function to handle the click of the hamburger menu
  const handleClick = () => {
    if(isClicked==="outer"){
    setClick("inner")
    // console.log(isClicked)
    }else{
    setClick("outer")
    // console.log(isClicked)
    }
  }

  return (
    <div>
      <NavBar clicked={isClicked}/>
      <SideBar mcq subjects markingSchemes answerPapers clicked={isClicked} onClickFunc={handleClick}/>
      <MarkingSchemeConfigure clicked={isClicked} data={markings} subjectId={subjectId}/>
      
    </div>
  )
}

export default MarkingSchemeConfigurePage
