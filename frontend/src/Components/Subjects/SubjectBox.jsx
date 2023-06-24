import {Link, useLocation} from 'react-router-dom';
function SubjectBox({subjectName,subjectCode,year}) {
  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')
  console.log("Hello::"+location);
  var formattedString="";
  if(year){
    formattedString = year;
  }else{
    formattedString = `${subjectCode}-${subjectName}`;
  }
  return (
    <div className='h-28 w-56 mr-6 mb-8 rounded-lg'>
      <div className='h-14 rounded-t-lg bg-[#4457FF]'></div>
      <div className= 'w-56 text-sm p-2 bg-[#D9D9D9] rounded-b-lg'>
      {formattedString}
      </div>
    </div>
  )
}

export default SubjectBox
