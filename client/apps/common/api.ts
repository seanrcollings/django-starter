import { useGet } from ".";

export interface UserType {
  id: number;
  username: string;
  email: string;
}

export function getUsers() {
  return useGet<UserType[]>("/api/users/");
}

export function getUser(id: number) {
  return useGet<UserType>(`/api/users/${id}/`);
}
