import { Route, Routes } from 'react-router-dom';
import TopBar from "./Components/TopBar";
import QuestionsPage from "./Pages/QuestionsPage";
import EssayPage from './Pages/EssayPage';
import McqPage from './Pages/McqPage';
import './Components/TopBar.css';
import TeacherPage from './Pages/TeacherPage';
import TeacherPasswordChange from './Pages/TeacherPasswordChange';
import ConfigureMarks from './Pages/ConfigureMarks';

function App(){
  return(
    <div>
      {/* <TopBar /> */}
      <Routes>
        <Route path="/" element={<QuestionsPage />} />
        <Route path="/teacherPasswordChange" element={<TeacherPasswordChange />} />
        <Route path="essayPage" element={<EssayPage />} />
        <Route path="mcqPage" element={<McqPage />} />
        <Route path="teacherPage" element={<TeacherPage />} />
        <Route path="/configureMarks" element={<ConfigureMarks />} />
      </Routes>
    </div>
  );
}

export default App;
