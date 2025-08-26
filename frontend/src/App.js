import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import Dashboard from './components/Dashboard';

function App() {
    return (
        <Router>
            <div>
                <h1>Autenticador de usuário</h1>
                <Switch>
                    <Route path="/register" component={Register} />
                    <Route path="/login" component={Login} />
                    <Route path="/dashboard" component={Dashboard} />
                    <Route path="/" exact>
                        <h2>Bem vindo (a)! Por favor, faça o registro ou login.</h2>
                    </Route>
                </Switch>
            </div>
        </Router>
    );
}

export default App;