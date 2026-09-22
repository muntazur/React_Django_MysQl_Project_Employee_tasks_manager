import { useState, useEffect } from "react";
import api from "./api";

function ReadFromApi(){
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        api.get('tasks/').then(response => {
            setTasks(response.data);
        }).catch(error => {
            console.error(error);
        });
        
    }, []);



    return (

        <>

            <h2>Employee Task Manager</h2>
            {
                tasks.map(task => {

                <table> 
                    <thead>
                        <th>Task_Title</th>
                        <th>Description</th>
                        <th>Status</th>
                    </thead>

                    <tbody>
                        <tr key={task.id}>
                            <td>{task.title}</td>
                            <td>{task.description}</td>
                            <td>{task.status}</td>
                        </tr>
                    </tbody>

                </table>
                    
                })
            }

        </>
           
    );
    
    
}