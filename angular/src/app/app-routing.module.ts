import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RestrictedComponent } from './restricted/restricted.component';
import { PublicComponent } from './public/public.component';


const routes: Routes = [
  {path: 'public', component: PublicComponent},
  {path: 'restricted', component: RestrictedComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
