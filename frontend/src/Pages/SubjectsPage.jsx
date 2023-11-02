import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import Subjects from '../Components/Subjects/Subjects'
import {useEffect, useState} from 'react'
import { MoonLoader } from 'react-spinners';
import axios from 'axios'
// import { set } from 'mongoose';

function SubjectsPage() {
  setTimeout(() => {
    // Timeout of 1s
  }, 1000);
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  if(!allItems){
    window.location.href="/";
  }
  // console.log(allItems);
  const user_id=allItems['user_id'];
  const userType = allItems['user_role'];
  console.log(userType,user_id);
  const accessToken = localStorage.getItem('accessToken')
  const [isClicked,setClick] = useState("inner");
  const [subjects,setSubjects] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(()=>{
    fetchSubjects();
  },[]);

  const fetchSubjects = async () =>{
      const headers = {
        Authorization: `Bearer ${accessToken}`,
      };
      //****Methana subjects code eken group karaganna oona
      // console.log(headers)
      if(userType==="admin"){
        axios
        .get(`http://127.0.0.1:8000/api_v1/admins/subjects`, {headers})
        .then((response) => {
          const data = response.data;
          console.log(data);
          setSubjects(data);
          const sortedData = [...data].sort((a, b) => a.subjectName.localeCompare(b.subjectName));
          setSubjects(sortedData)
          setIsLoading(false);
        })
        .catch((error) => {
          console.log(error.response.status);
          if(error.response.status===404){
            setSubjects(null);
            setIsLoading(false);
          }
        });
      }else if(userType==="teacher"){
        // console.log(headers);
        axios
        .get(`http://127.0.0.1:8000/api_v1/subjects/${user_id}`, {headers})
        .then((response) => {
          const data = response.data;
          setSubjects(data);
          const sortedData = [...data].sort((a, b) => a.subjectName.localeCompare(b.subjectName));
          setSubjects(sortedData)
          setIsLoading(false);
        })
        .catch((error) => {
          console.log(error.response.status);
          if(error.response.status===404){
            setSubjects(null);
            setIsLoading(false);
          }
        });
      }
    
  }

  // if (isLoading) {
  //   return <div>Loading...</div>;
  // }
  // console.log("Subjects:",subjects)
  //Function to handle the click of the hamburger menu
  const handleClick = () => {
    if(isClicked==="outer"){
    setClick("inner")
    }else{
    setClick("outer")
    }
    // console.log(isClicked)
  }
  const config = [
    {
      label:"subjectCode"
    },
    {
      label:"subjectName"
    }
  ]

  return (
    <div className='h-[100vh]'>
      <NavBar black onClickFunc={handleClick} clicked={isClicked}/>
      <SideBar mcq subjects markingSchemes answerPapers clicked={isClicked} onClickFunc={handleClick}/>
      {isLoading ? <MoonLoader color="#4457FF" height={6} width={128} className='absolute top-[20vw] left-[55%]'/> 
        :<Subjects clicked={isClicked} data={subjects}/>
      }
      
    </div>
  )
}

export default SubjectsPage
