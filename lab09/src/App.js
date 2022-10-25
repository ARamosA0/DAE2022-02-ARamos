import { useState } from 'react';
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {



  const [articulo, setArticulo] = useState([
    {
        codigo: 1, 
        descripcion: 'coca-cola',
        precio: 2.50
   },{
        codigo: 2, 
        descripcion: 'inka-cola',
        precio: 2.20
   },{
        codigo: 3, 
        descripcion: 'fanta',
        precio: 1.70
   }])

   const borrar = (cod) =>{
      const temp = articulo.filter((el)=>el.codigo !== cod)
      console.log(temp)
      setArticulo(temp)
   }

  return (
    <>
      <Table striped bordered hover>
      <thead>
        <tr>
          <th>Codigo</th>
          <th>Descripción</th>
          <th>Precio</th>
          <th>Borra?</th>
        </tr>
      </thead>
      <tbody>
        {articulo.length > 0 &&
        articulo.map((art,index)=>(
          <tr key={art.codigo}>
            <td value={art.codigo}>
              {art.codigo}
            </td>
            <td>
              {art.descripcion}
            </td>
            <td>
              {art.precio}
            </td>
            <td>
              <Button onClick={()=>borrar(art.codigo)} variant="primary">Borrar</Button>
            </td>
          </tr>
        ))}
      </tbody>
    </Table>
    </>
  );
}

export default App;

