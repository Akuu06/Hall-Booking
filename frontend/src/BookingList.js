import React,{useEffect,useState} from "react";
import axios from "axios";
function BookingList(){
 const [data,setData]=useState([]);
 useEffect(()=>{axios.get("http://127.0.0.1:8000/api/bookings/").then(r=>setData(r.data));},[]);
 return (<div><h2>Hall Bookings</h2><ul>{data.map(b=><li key={b.id}>{b.applicant_name}</li>)}</ul></div>);
}
export default BookingList;
