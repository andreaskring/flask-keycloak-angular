import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RestrictedComponent } from './restricted/restricted.component';
import { PublicComponent } from './public/public.component';
import { AuthGuard } from './auth/auth.guard';


const routes: Routes = [
  {path: 'public', component: PublicComponent},
  {path: 'restricted', component: RestrictedComponent, canActivate: [AuthGuard]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
