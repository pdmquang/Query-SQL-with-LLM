// src/Table.tsx

import React from 'react';

const Table: React.FC = () => {
    return (
        <table>
            <thead>
                <tr>
                    <th>A</th>
                    <th>B</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Description of A</td>
                    <td>Description of B</td>
                </tr>
                <tr>
                    <td>Value of A</td>
                    <td>Value of B</td>
                </tr>
            </tbody>
        </table>
    );
};

export default Table;