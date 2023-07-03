import {Link, useLocation} from 'react-router-dom';
function Table({name, role, date, subjects, select, index, fileName, overallMark, MarkingSchemes,teachers, AnswerSheets, papers}) {
  console.log("teacher:",teachers)
  const handleSelect = () =>{
    console.log({select});
  }

  let teacher =""
  let markingscheme =""
  let paper =""
  let AnswerSheet =""
  if(teachers){
    teacher = teachers.map((teacher) => {
        return (
          <tr className="w-full">
            <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>{teacher.firstName} {teacher.lastName}</td>
            <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>{teacher.role}</td>
            {/* {date && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-4 font-medium opacity-60'>{teacher.date}</td>} */}
            <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-4 font-medium opacity-60'>2023</td>
            {/* {subjects && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>{teacher.subjects}</td>} */}
            <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>3</td>
            {/* {select && <td className=' flex justify-center text-sm px-4 py-2 h-12 border-y-2 border-x-2 font-medium'><button className="rounded rounded-xl bg-[#4457FF] w-32 max-sm:w-20 h-8 mr-2 text-white flex justify-center items-center flex-row" onClick={handleSelect}><div className='ml-2'>Select</div></button></td>} */}
          </tr>
        )
      })
  }

  if(MarkingSchemes){
    console.log("MarkingSchemes:",MarkingSchemes)
    markingscheme = (
        <tr className="w-full">
          <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>{MarkingSchemes.subjectCode}-{MarkingSchemes.subjectName}-{MarkingSchemes.year}</td>
          <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-4 font-medium opacity-60'>10/06/2023</td>
          <td className=' flex justify-center text-sm px-4 py-2 h-12 border-y-2 border-x-2 font-medium'><button className="rounded rounded-xl bg-[#4457FF] w-32 max-sm:w-20 h-8 mr-2 text-white flex justify-center items-center flex-row" onClick={handleSelect}><div className='ml-2'>Select</div></button></td>
        </tr>
      )
  }

  // if(papers){
  //   paper = papers.map((paper) => {
  //     return (
  //       <Link key={paper._id} to={"/subjects/marks/"+paper.year+"/"+paper.subjectId}>
  //         <tr className="w-full">
  //           <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>{paper.paper}</td>
  //           <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>{paper.paper}</td>
  //           {/* {date && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-4 font-medium opacity-60'>{teacher.date}</td>} */}
  //           <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-4 font-medium opacity-60'>100</td>
  //           {/* {subjects && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>{teacher.subjects}</td>} */}
  //           {/* <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>3</td> */}
  //           {/* {select && <td className=' flex justify-center text-sm px-4 py-2 h-12 border-y-2 border-x-2 font-medium'><button className="rounded rounded-xl bg-[#4457FF] w-32 max-sm:w-20 h-8 mr-2 text-white flex justify-center items-center flex-row" onClick={handleSelect}><div className='ml-2'>Select</div></button></td>} */}
  //         </tr>
  //       </Link>
  //     )
  //   })
  // }

  if(AnswerSheets){
    AnswerSheet = AnswerSheets.map((AnswerSheet) => {
      return (
        <tr className="w-full" key={AnswerSheet.subjectId}>
            
            <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60 w-2/5'><Link key={AnswerSheet.id} to={"/subjects/marks/"+AnswerSheet.year+"/"+AnswerSheet.subjectId} className='w-full'>{AnswerSheet.paper}</Link></td>
            <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60 w-3/12'><Link key={AnswerSheet.id} to={"/subjects/marks/"+AnswerSheet.year+"/"+AnswerSheet.subjectId} className='w-full'>{AnswerSheet.paper}</Link></td>
            {/* {date && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-4 font-medium opacity-60'>{teacher.date}</td>} */}
            <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-4 font-medium opacity-60 w-3/12'><Link key={AnswerSheet.id} to={"/subjects/marks/"+AnswerSheet.year+"/"+AnswerSheet.subjectId} className='w-full'>100</Link></td>
            {/* {subjects && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>{teacher.subjects}</td>} */}
            {/* <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>3</td> */}
            {/* {select && <td className=' flex justify-center text-sm px-4 py-2 h-12 border-y-2 border-x-2 font-medium'><button className="rounded rounded-xl bg-[#4457FF] w-32 max-sm:w-20 h-8 mr-2 text-white flex justify-center items-center flex-row" onClick={handleSelect}><div className='ml-2'>Select</div></button></td>} */}
        
          </tr>
      )
    })
  }

    return (
    <div className='w-full max-sm:px-4 overflow-auto'>
      <table className='w-full'>
        <thead className='bg-[#D9D9D9] sticky'>
        <tr className="w-full">
          {name && <th className='text-xl h-8 font-bold opacity-60 w-2/5'>Name</th>}
          {role && <th className='text-xl h-8 font-bold opacity-60 w-1/5'>Role</th>}

          {date && <th className='text-xl h-8 font-bold opacity-60 w-1/5'>Date Added</th>}
          {subjects && <th className='text-xl h-8 font-bold opacity-60 w-2/5'>Subjects</th>}

          {index && <th className='text-xl h-8 font-bold opacity-60 w-3/12'>Index</th>}
          {fileName && <th className='text-xl h-8 font-bold opacity-60 w-3/12'>File Name</th>}
          {overallMark && <th className='text-xl h-8 font-bold opacity-60 w-3/12'>Overall Mark</th>}
         
          {select && <th className='text-xl h-8 font-bold opacity-60 w-3/12'>Select</th>}

        </tr>
        </thead>
        <tbody>
            {/* <tr className="w-full"> */}

              {/* {name && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'></td>} */}
              {/* {date && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-4 font-medium opacity-60'>10/06/2023</td>} */}
              {/* {MarkingSchemes && name && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>{MarkingSchemes.subjectCode}-{MarkingSchemes.subjectName}-{MarkingSchemes.year}</td>} */}


              {/* {index && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>18000000</td>}
              {fileName && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>DSA-2023</td>}
              {overallMark && <td className='text-lg px-4 max-sm:px-1 h-12 border-y-2 border-x-2 font-medium opacity-60'>100%</td>} */}

            


              {/* {select && <td className=' flex justify-center text-sm px-4 py-2 h-12 border-y-2 border-x-2 font-medium'><button className="rounded rounded-xl bg-[#4457FF] w-32 max-sm:w-20 h-8 mr-2 text-white flex justify-center items-center flex-row" onClick={handleSelect}><div className='ml-2'>Select</div></button></td>} */}
              {teacher}
              {markingscheme}
              {paper}
              {AnswerSheet}
            {/* </tr> */}
        </tbody>
      </table>
    </div>
  )
}

export default Table
