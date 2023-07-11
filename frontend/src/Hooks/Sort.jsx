function Sort() {
  return (
    <div>
      
    </div>
  )
}

function useSort(data,label,sortOrder){
    // const sortValue = data.filter(column=>column.subjectCode==="subjectCode")
    // console.log("SortValue",sortValue)
    // const sortedData = [...data].sort((a,b)=>{
    //     const valueA = sortValue(a);
    //     const valueB = sortValue(b);

    //     const reverseOrder = sortOrder ==='asc' ? 1 : -1;

    //     if(typeof valueA === 'string'){
    //         return valueA.localeCompare(valueB) * reverseOrder
    //     }else{
    //         return (valueA - valueB) * reverseOrder
    //     }
    // })
    const sortedData = [...data].sort((a, b) => a.subjectCode.localeCompare(b.subjectCode));
    return sortedData;
}

export default Sort;
export {useSort}
