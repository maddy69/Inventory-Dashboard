import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Dashboard.css'; 

const Dashboard = () => {
    const [inventory, setInventory] = useState([]);

    useEffect(() => {
        axios.get('/api/inventory/')
            .then(response => {
                console.log('Fetched data:', response.data);
                setInventory(response.data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []);

    const calculateTotalMSRP = (items) => {
        return items.reduce((total, item) => total + item.price, 0).toFixed(2);
    };

    const calculateAverage = (items) => {
        return items.length ? (calculateTotalMSRP(items) / items.length).toFixed(2) : 0;
    };

    const newInventory = inventory.filter(item => item.condition.trim().toUpperCase() === 'NEW');
    const usedInventory = inventory.filter(item => item.condition.trim().toUpperCase() === 'USED');
    const cpoInventory = inventory.filter(item => item.condition.trim().toUpperCase() === 'CPO');

    return (
        <div className="dashboard-container">
            <h1 className="main-title">Inventory Dashboard</h1>

            <div className="section">
                <h2>Recent Data</h2>
                <div className="recent-data">
                    {inventory.slice(0, 5).map(item => (
                        <div key={item.id} className="item">
                            <p>{item.title} - ${item.price}</p>
                        </div>
                    ))}
                </div>
            </div>

            <div className="section">
                <h2>Inventory Count</h2>
                <div className="inventory-count">
                    <p>NEW: {newInventory.length}</p>
                    <p>USED: {usedInventory.length}</p>
                    <p>CPO: {cpoInventory.length}</p>
                </div>
            </div>

            <div className="section">
                <h2>Average MSRP</h2>
                <div className="average-msrp">
                    <p>NEW: ${calculateAverage(newInventory)}</p>
                    <p>USED: ${calculateAverage(usedInventory)}</p>
                    <p>CPO: ${calculateAverage(cpoInventory)}</p>
                </div>
            </div>

            <div className="section">
                <h2>History Log</h2>
                <table className="history-log">
                    <thead>
                        <tr>
                            <th>Condition</th>
                            <th>Count</th>
                            <th>Total MSRP</th>
                            <th>Average MSRP</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>NEW</td>
                            <td>{newInventory.length}</td>
                            <td>${calculateTotalMSRP(newInventory)}</td>
                            <td>${calculateAverage(newInventory)}</td>
                        </tr>
                        <tr>
                            <td>USED</td>
                            <td>{usedInventory.length}</td>
                            <td>${calculateTotalMSRP(usedInventory)}</td>
                            <td>${calculateAverage(usedInventory)}</td>
                        </tr>
                        <tr>
                            <td>CPO</td>
                            <td>{cpoInventory.length}</td>
                            <td>${calculateTotalMSRP(cpoInventory)}</td>
                            <td>${calculateAverage(cpoInventory)}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default Dashboard;
