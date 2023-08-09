import classnames from 'classnames';
import SubjectBox from './Subjects/SubjectBox';
import {Link, useLocation} from 'react-router-dom';
function Years({clicked,data}) {
  const classes = classnames('sidebar py-4 top-[8%] h-[92%] max-sm:ml-16');

  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')
  // console.log(pathName[0]);
  const subjects = data.map((subject,index)=>{
    // console.log(subject);
    return <Link key={index} to={"/"+pathName[0]+"/"+subject?.year+"/"+subject?.id} className='h-40 w-80'><SubjectBox key={index} subject={subject} backgroundUrl={subject.backgroundImage} subjectCode={subject.subjectCode} subjectName={subject.subjectName}  year={subject?.year} /></Link>
  })
  console.log("Years::"+clicked);
  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
      <div className={`flex justify-center items-center`}>
          <div className='h-[85%] w-11/12'>
            <div className='flex flex-row items-center justify-between px-10 h-10 mb-8'>
                <p className='bg-black/20 p-2 rounded rounded-lg'>Year</p>
                <p className='bg-black/20 p-2 rounded rounded-lg'>Grade</p>
            </div>
            
            <div className='flex flex-wrap justify-between gap-4 overflow-auto'>
              {subjects}
            </div>
          </div>
      </div>
    </div>
  )
}

export default Years
