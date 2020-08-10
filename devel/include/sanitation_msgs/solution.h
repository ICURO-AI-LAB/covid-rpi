// Generated by gencpp from file sanitation_msgs/solution.msg
// DO NOT EDIT!


#ifndef SANITATION_MSGS_MESSAGE_SOLUTION_H
#define SANITATION_MSGS_MESSAGE_SOLUTION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace sanitation_msgs
{
template <class ContainerAllocator>
struct solution_
{
  typedef solution_<ContainerAllocator> Type;

  solution_()
    : status()
    , runtime()  {
    }
  solution_(const ContainerAllocator& _alloc)
    : status(_alloc)
    , runtime(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _status_type;
  _status_type status;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _runtime_type;
  _runtime_type runtime;





  typedef boost::shared_ptr< ::sanitation_msgs::solution_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sanitation_msgs::solution_<ContainerAllocator> const> ConstPtr;

}; // struct solution_

typedef ::sanitation_msgs::solution_<std::allocator<void> > solution;

typedef boost::shared_ptr< ::sanitation_msgs::solution > solutionPtr;
typedef boost::shared_ptr< ::sanitation_msgs::solution const> solutionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sanitation_msgs::solution_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sanitation_msgs::solution_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace sanitation_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sanitation_msgs': ['/home/ubuntu/Ubiquity-Pi/src/sanitation_msgs/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::sanitation_msgs::solution_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sanitation_msgs::solution_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sanitation_msgs::solution_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sanitation_msgs::solution_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sanitation_msgs::solution_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sanitation_msgs::solution_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sanitation_msgs::solution_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cccbed84ab87ac04d9a21ce3df5e3ac7";
  }

  static const char* value(const ::sanitation_msgs::solution_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xcccbed84ab87ac04ULL;
  static const uint64_t static_value2 = 0xd9a21ce3df5e3ac7ULL;
};

template<class ContainerAllocator>
struct DataType< ::sanitation_msgs::solution_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sanitation_msgs/solution";
  }

  static const char* value(const ::sanitation_msgs::solution_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sanitation_msgs::solution_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string status\n\
string runtime\n\
";
  }

  static const char* value(const ::sanitation_msgs::solution_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sanitation_msgs::solution_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.status);
      stream.next(m.runtime);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct solution_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sanitation_msgs::solution_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sanitation_msgs::solution_<ContainerAllocator>& v)
  {
    s << indent << "status: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.status);
    s << indent << "runtime: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.runtime);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SANITATION_MSGS_MESSAGE_SOLUTION_H
